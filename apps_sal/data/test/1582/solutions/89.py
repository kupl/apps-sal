N = int(input())
(a, b) = divmod(N, 10)


def h(n):
    return h(n // 10) if n > 9 else n


print(a ** 2 + 8 + sum(((h(i) <= b) * (i % 10 == h(N)) * (1 + (a != i // 10)) for i in range(1, N + 1))) if a else N)
