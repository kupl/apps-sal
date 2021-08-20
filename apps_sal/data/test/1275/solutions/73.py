(N, K) = map(int, input().split())


def f(t):
    if 2 <= t <= N + 1:
        return t - 1
    elif N + 1 <= t <= 2 * N:
        return 2 * N + 1 - t
    else:
        return 0


s = 0
for y in range(2, 2 * N + 1):
    s += f(y) * f(y + K)
print(s)
