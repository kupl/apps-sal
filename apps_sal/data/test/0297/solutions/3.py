import math
import sys
from itertools import permutations


def mp():
    return list(map(int, input().split()))


debug = 0
if debug:
    file = open("input.txt", "r")
    input = file.readline
else:
    input = sys.stdin.readline


def main():
    n, m, k = mp()
    x = n * m
    g = math.gcd(x, k)
    x //= g
    a = 0
    if k // g == 1:
        a = x * 2
    elif k // g == 2:
        a = x
    else:
        print("NO")
        return
    print("YES")
    kn = math.gcd(k, n)
    k //= kn
    km = math.gcd(k, m)
    on = n
    om = m
    n //= kn
    m //= km
    t = a // (n * m)
    if t * n <= on:
        print(0, 0)
        print(t * n, 0)
        print(0, m)
    elif t * m <= om:
        print(0, 0)
        print(n, 0)
        print(0, m * t)
    else:
        # assert(t == 4)
        print(0, 0)
        print(2 * n, 0)
        print(0, 2 * m)


main()
