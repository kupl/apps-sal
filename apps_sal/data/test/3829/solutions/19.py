import math


def solve():
    [m, n] = [int(x) for x in input().split()]

    ans = 0
    for i in range(m):
        ans += pow(i / m, n)

    ans = m - ans
    print(ans)

def __starting_point():
    solve()





__starting_point()
