from collections import defaultdict as dd
import math
import sys
input = sys.stdin.readline


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n, m = mi()

a_s = lm()

b_s = lm()

elim = []


for power in reversed(list(range(0, 10))):
    bad = False
    for a in a_s:
        found = False
        for b in b_s:
            b_bad = False
            for pre_pow in elim:
                if a & (1 << pre_pow) and b & (1 << pre_pow):
                    b_bad = True
            if a & (1 << power) and b & (1 << power):
                #print(a, 1<<power)
                #print(b, 1<<power)
                b_bad = True
            if b_bad == False:
                found = True
        if not found:
            bad = True
            break
    # print(bad)
    if not bad:
        elim.append(power)
ans = 0
for i in range(0, 10):
    if i not in elim:
        ans += 2**i


print(ans)
