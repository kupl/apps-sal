from numpy import cumsum
n, m = map(int, input().split())
a = list(map(int, input().split()))
result = cumsum(a)[-1]
mi = result / (4 * m)
ans = 0
for i in range(n):
    if a[i] >= mi:
        ans += 1
if ans >= m:
    print('Yes')
else:
    print('No')
