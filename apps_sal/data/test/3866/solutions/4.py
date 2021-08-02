n = int(input())

if n % 2 == 0:
    print(-1)
else:
    print(" ".join(map(str, range(n))))
    print(" ".join(map(str, range(n))))
    print(" ".join(map(str, [2 * x % n for x in range(n)])))
