n = int(input())
l = list(map(int, input().split()))

mn = n-1 - l[-1]
ans = 1
for i in range(n-2, -1, -1):
    if i < mn:
        ans += 1
    mn = min(mn, i - l[i])
print(ans)
