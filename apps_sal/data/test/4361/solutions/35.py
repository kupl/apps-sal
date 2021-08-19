(n, k) = map(int, input().split())
l = [int(input()) for i in range(n)]
l.sort()
mi = float('INF')
for i in range(n - k + 1):
    sub = l[i + k - 1] - l[i]
    mi = min(mi, sub)
print(mi)
