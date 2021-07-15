x, u, y, v = list(map(int, input().split()))
N, M = y - x + 1, v - u + 1
n, m = (N >> 1) * (N&1), (M >> 1) * (M&1)
print((N - n)*(M - m) + n*m)

