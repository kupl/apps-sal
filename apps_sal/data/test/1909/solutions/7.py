(n, k) = map(int, input().split())
a = list(map(int, input().split()))
m = 1000000000
ans = 1
for i in range(k):
    mt = 0
    for j in range(i, n, k):
        mt += a[j]
    if mt < m:
        m = mt
        ans = i + 1
print(ans)
