n, m = list(map(int, input().split()))
ar = list(map(int, input().split()))
ar.sort()
ans = ar[n - 1] - ar[0]
for i in range(1, m - n + 1):
    ans = min(ans, ar[i + n - 1] - ar[i])
print(ans)
#print(ar)

