import sys
import math
f = sys.stdin


def modInverse(a, m):
    g = gcd(a, m)
    if g != 1:
        return None
    else:
        return power(a, m - 2, m)


def power(x, y, m):
    if y == 0:
        return 1
    p = power(x, y // 2, m) ** 2
    if y & 1 == 1:
        p *= x
    return p % m


def gcd(a, b):
    while a != 0:
        t = b % a
        b = a
        a = t
    return b


(n, m) = list(map(int, f.readline().split()))
s1 = list(map(int, f.readline().split()))
s2 = list(map(int, f.readline().split()))
pos = [1, 0]
all_pos = 1
for (a1, a2) in zip(s1, s2):
    next_pos = [0, 0]
    if a1 == 0 and a2 == 0:
        next_pos[0] += pos[0] * m
        next_pos[1] += pos[0] * m * (m - 1) // 2
        next_pos[1] += pos[1] * m * m
        all_pos *= m * m
    elif a1 == 0:
        next_pos[0] += pos[0]
        next_pos[1] += pos[0] * (m - a2)
        next_pos[1] += pos[1] * m
        all_pos *= m
    elif a2 == 0:
        next_pos[0] += pos[0]
        next_pos[1] += pos[0] * (a1 - 1)
        next_pos[1] += pos[1] * m
        all_pos *= m
    else:
        if a1 > a2:
            next_pos[1] += pos[0]
        elif a1 == a2:
            next_pos[0] += pos[0]
        next_pos[1] += pos[1]
    pos = next_pos
    if pos[0] == 0:
        break
    g = gcd(pos[0], all_pos)
    g = gcd(pos[1], g)
    pos[0] //= g
    pos[1] //= g
    all_pos //= g
    pos[0] %= 1000000007
    pos[1] %= 1000000007
    all_pos %= 1000000007
p = pos[1]
q = all_pos
pq_gcd = gcd(p, q)
p //= pq_gcd
q //= pq_gcd
q_inv = modInverse(q, 1000000007)
print(p * q_inv % 1000000007)
