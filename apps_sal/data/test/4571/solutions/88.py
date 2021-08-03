N, M = map(int, input().split())


def f(a, r, c):
    return (a / (1 - r) + (a * r) / (1 - r)**2) * c


a = 1 / 2**M
r = (2**M - 1) / 2**M
c = 1900 * M + 100 * (N - M)

print(int(f(a, r, c)))
