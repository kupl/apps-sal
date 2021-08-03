def fine():
    f, c, n = 1, 1, 1
    yield 0
    while True:
        yield f
        n += 1
        c = c * (4 * n - 6) // n
        f = (c - f) // 2


f = fine()
n = int(input())
print((sum(next(f) for _ in range(n + 3)) - 1) % (10**9 + 7))
