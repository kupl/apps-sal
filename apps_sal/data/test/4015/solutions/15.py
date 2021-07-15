ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n, m = mi()
if m % n == 0:
    d = m // n
    c2 = c3 = 0
    while d % 2 == 0:
        c2 += 1
        d //= 2
    while d % 3 == 0:
        c3 += 1
        d //= 3
    print(c2 + c3 if d == 1 else -1)
else:
    print(-1)
