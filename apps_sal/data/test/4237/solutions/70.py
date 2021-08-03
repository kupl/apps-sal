import sys


def gcd(a, b):
    """
    最大公約数を求める
    """
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    最小公倍数を求める
    """
    return a * b // (gcd(a, b))


input = sys.stdin.readline

a, b, c, d = list(map(int, input().split()))

div_ac = (a - 1) // c
div_bc = b // c


div_ad = (a - 1) // d
div_bd = b // d

lcm_cd = lcm(c, d)

div_acd = (a - 1) // lcm_cd
div_bcd = b // lcm_cd

a_1_result = div_ac + div_ad - div_acd
b_result = div_bc + div_bd - div_bcd

print(((b + 1 - a) - (b_result - a_1_result)))
