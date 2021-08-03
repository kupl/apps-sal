import math
from datetime import date


def f(x, a):
    ans = 0
    for y in a:
        ans += (x - y) ** 2

    return ans


def main():

    n = int(input())
    a = [int(x) for x in input().split()]
    s = 0
    for x in a:
        s += x

    s = s // n
    ans = 10**17

    for x in range(s - 2, s + 3):
        ans = min(ans, f(x, a))

    print(ans)


main()
