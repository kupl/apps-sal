n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
m = int(input())
a.sort()
ans = 0
for i in range(m):
    if (i < n):
        ans += a[i]
    else:
        ans -= d
print(ans)
