"""
Created on Sun Apr  2 22:42:34 2017

@author: Sean38
"""

n = int(input().rstrip())
s = input()
a = [int(ch) for ch in s.split()]
a = a[0:n]
a.sort()


def check_num(p, i):

    max_b = (i // (p + 1))
    b = i % p + ((max_b - i % p) // p) * p
    cur = (i - b) // p

    if b < 0:
        return None
    return cur


def sets_num(p):

    total = 0
    for i in a:
        if check_num(p, i):
            total += check_num(p, i)
        else:
            return None
    return total


for div_sets in range(1, a[0] + 1):
    p, q = divmod(a[0], div_sets)
    if (q == 0):
        if sets_num(p):
            print(sets_num(p))
            break
        if (p > 0) and sets_num(p - 1):
            print(sets_num(p - 1))
            break
    else:
        if sets_num(p):
            print(sets_num(p))
            break
