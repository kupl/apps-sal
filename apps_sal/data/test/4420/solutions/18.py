for _ in range(int(input())):
    (x, y, n) = map(int, input().split())
    r = n % x
    if r < y:
        n -= n % x + 1
    n -= n % x - y
    print(n)
