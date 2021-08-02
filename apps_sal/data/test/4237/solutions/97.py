import math


def cnt(a: int, k: int):
    return a // k


def num(a, c, d):
    m_a_c = cnt(a, c)
    m_a_d = cnt(a, d)
    m_a_cd = cnt(a, c * d // math.gcd(c, d))
    return a - m_a_c - m_a_d + m_a_cd


a, b, c, d = list(map(int, input().split()))
print((num(b, c, d) - num(a - 1, c, d)))
