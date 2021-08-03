n = int(input())
if n % 2 == 0:
    print(int(n * 1.5))
    print(*list(range(1, n + 1, 2)), end=' ')
    print(*list(range(2, n + 1, 2)), end=' ')
    print(*list(range(1, n + 1, 2)), end=' ')
else:
    print(3 * (n // 2) + 1)
    print(*list(range(2, n + 1, 2)), end=' ')
    print(*list(range(1, n + 1, 2)), end=' ')
    print(*list(range(2, n + 1, 2)), end=' ')
