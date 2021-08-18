n = int(input())
if n % 2 == 0:
    print(-1)
else:
    print(*list(range(n)))
    print(*list(range(n)))
    print(*list(map(lambda x, y: (x + y) % n, list(range(n)), list(range(n)))))
