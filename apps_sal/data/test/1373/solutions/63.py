(N, K) = map(int, input().split())


def f(i):
    return i * (i + 1) // 2


print(sum((f(N) - f(N - i) - f(i - 1) + 1 for i in range(K, N + 2))) % (10 ** 9 + 7))
