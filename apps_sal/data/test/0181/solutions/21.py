import sys
import math


def main():
    n = int(input())
    n = -n
    n %= 360
    a = n
    a1 = 360 - a
    b = (a + 90) % 360
    b1 = 360 - b
    c = (b + 90) % 360
    c1 = 360 - c
    d = (c + 90) % 360
    d1 = 360 - d
    ans = min([a, a1, b, b1, c, c1, d, d1])
    if a == ans or a1 == ans:
        print(0)
    elif b == ans or b1 == ans:
        print(1)
    elif c == ans or c1 == ans:
        print(2)
    elif d == ans or d1 == ans:
        print(3)


main()
