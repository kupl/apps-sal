from bisect import bisect_left

n, k = map(int, input().split())
a = [int(x) for x in input().split()]
sa = sorted(a)

ans = [0] * n
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if a[x] > a[y]:
        ans[x] -= 1
    if a[y] > a[x]:
        ans[y] -= 1

for i in range(n):
    t = bisect_left(sa, a[i])
    ans[i] += t
    print(ans[i], end=' ')

