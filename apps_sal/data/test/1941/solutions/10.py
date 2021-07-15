f = lambda: map(int, input().split())
A, B, n = f()
for i in range(n):
    l, t, m = f()
    S = 2 * (A + B * l) - B
    T = S - B - 2 * m * t
    r = l + int(((S * S - 4 * B * T) ** 0.5 - S) / (2 * B))
    r = min(r, (t - A) // B + 1)
    print(-1 if r < l else r)
