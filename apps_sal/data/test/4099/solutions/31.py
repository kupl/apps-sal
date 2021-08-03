n, k, m = map(int, input().split())
a = list(map(int, input().split()))
ai = 0
for i in range(n - 1):
    ai += a[i]
ans = n * m - ai
if ai < n * m and ans <= k:
    print(ans)
elif ai < n * m and ans > k:
    print(-1)
else:
    print(0)
