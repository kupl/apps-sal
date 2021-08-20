(n, m, k) = map(int, input().split())
dist = 10000000000.0
a = [int(i) for i in input().split()]
for i in range(n):
    if a[i] > 0 and a[i] <= k:
        dist = min(dist, abs(m - 1 - i))
print(dist * 10)
