(n, k) = map(int, input().split())
h = [int(input()) for _ in range(n)]
h = sorted(h)
hmin = 10000000000.0
for i in range(n - k + 1):
    hmin = min(hmin, h[i + k - 1] - h[i])
print(hmin)
