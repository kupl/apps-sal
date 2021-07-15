from math import *


def solve():
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))

    mn = min(abs(x), abs(y))
    ans = 0
    if b < 2 * a:
        ans += b * (mn)
        if x == mn:
            x = 0
            if y > 0:
                y -= mn
            else:
                y += mn
            ans += a * abs(y)
            print(ans)
        else:
            y = 0
            if x > 0:
                x -= mn
            else:
                x += mn
            ans += a * abs(x)
            print(ans)
    else:
        print(a * (abs(x) + abs(y)))


for _ in range(int(input())):
    solve()

