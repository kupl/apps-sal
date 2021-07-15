import math

def check(n, top):
    for x in range(2, top+1):
        if n % x == 0:
            return False
    return True


def __starting_point():
    p, y = input().split()
    p = int(p)
    y = int(y)

    m = min(math.floor(math.sqrt(y)),p)

    cur = y
    while cur > p:
        if check(cur, m):
            print(cur)
            return
        cur -= 1

    print(-1)

__starting_point()
