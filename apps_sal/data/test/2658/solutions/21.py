(n, k) = map(int, input().split())
a = list(map(int, input().split()))
dist = [0 for i in [0] * (n + 1)]
idx = 1
d = 1
while not dist[idx] and d < k + 1:
    dist[idx] = d
    idx = a[idx - 1]
    d += 1
if d == k + 1:
    print(idx)
else:
    rem = dist[idx] - 1
    cyc = d - dist[idx]
    k -= rem
    k %= cyc
    for i in range(k):
        idx = a[idx - 1]
    print(idx)
