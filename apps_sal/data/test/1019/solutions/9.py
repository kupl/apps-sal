import sys
from fractions import gcd


def main():
    n = int(input())
    a = n // 2
    if n % 2 == 0:
        a -= 1

    b = n - a
    while gcd(a, b) > 1:
        a -= 1
        b += 1
    print(a, b)


main()

