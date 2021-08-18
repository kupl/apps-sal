import math


def INT(): return int(input())
def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())
def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    a, b, c, d = INTM()
    lcm = (c * d) // math.gcd(c, d)
    a -= 1
    ct_a = a - (a // c) - (a // d) + (a // lcm)
    ct_b = b - (b // c) - (b // d) + (b // lcm)
    print(ct_b - ct_a)


def __starting_point():
    do()


__starting_point()
