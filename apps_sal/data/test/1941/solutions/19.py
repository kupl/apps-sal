def f(): return list(map(int, input().split()))


A, B, n = f()

k = 0.5

for i in range(n):

    l, t, m = f()

    b = A / B + l - k

    c = b - k - (m * t) / B

    r = min(l + int((b * b - 2 * c) ** k - b), (t - A) // B + 1)

    print(-1 if r < l else r)
