n = int(input())

if n % 2 == 0:
    print(-1)
else:
    print(*list(range(n)))
    print(*list(range(n)))
    print(*((i + i) % n for i in range(n)))
