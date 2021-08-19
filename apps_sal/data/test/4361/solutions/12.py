(n, k) = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
dh = [int(1000000000.0)] * n
for i in range(k - 1, n):
    dh[i] = h[i] - h[i - k + 1]
print(min(dh))
