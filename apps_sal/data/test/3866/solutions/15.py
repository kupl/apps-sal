n = int(input())

if n % 2 == 0:
    print(-1)
else:
    print(*list(range(n)))
    print(*list(range(1, n)), 0)
    print(*list(range(1, n, 2)), *list(range(0, n, 2)))

