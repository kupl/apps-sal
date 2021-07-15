from math import sqrt

# import sys
# from io import StringIO
# sys.stdin = StringIO(open(__file__.replace('.py', '.in')).read())

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0:
        print(1, 1)
        continue

    sq = int(sqrt(n)) + 1
    while sq * sq <= 2 * n:
        zs = sqrt(sq * sq - n)
        if zs.is_integer():
            m = sq // zs
            if sq * sq - (sq // m) ** 2 == n:
                print(sq, int(m))
                break
        sq += 1
    else:
        print(-1)

