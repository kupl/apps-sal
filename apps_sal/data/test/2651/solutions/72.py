mod = 10 ** 9 + 7


def solve(N, X):
    return sum((2 * k - N + 1) * x for k, x in enumerate(X)) % mod


N, M, *XY = map(int, open(0).read().split())
X, Y = XY[:N], XY[N:]

print(solve(N, X) * solve(M, Y) % mod)
