# -*- coding: utf-8 -*-


def solve():
    n, m = list(map(int, input().split()))
    p = input()
    if m == 0:
        return powmod(n)
    delta = len(p) - 1
    ys = list(map(int, input().split()))
    tail = 0
    free_chars = 0
    for y in ys:
        if y > tail:
            free_chars += y - tail - 1
        elif not is_consistent(p, tail - y + 1):
            return 0
        tail = y + delta
    free_chars += n - tail
    return powmod(free_chars)

ok_set = set()
def is_consistent(p, margin):
    nonlocal ok_set
    if margin in ok_set:
        return True
    elif p[:margin] == p[-margin:]:
        ok_set.add(margin)
        return True
    else:
        return False


def powmod(p):
    mod = 10**9 + 7
    pbin = bin(p)[2:][-1::-1]
    result = 26 if pbin[0] == '1' else 1
    tmp = 26
    for bit in pbin[1:]:
        tmp *= tmp
        tmp %= mod
        if bit == '1':
            result *= tmp
            result %= mod
    return result


print(solve())

