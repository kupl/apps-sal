from itertools import permutations
import sys
from math import *
from fractions import gcd
def readints(): return list(map(int, input().strip('\n').split()))


n = input().strip('\n')

perms = [''.join(p) for p in permutations('1689')]
mod = {}
for p in perms:
    p = int(p)
    mod[p % 7] = p


freq = [0] * 10
for d in n:
    d = int(d)
    freq[d] += 1


for d in (1, 6, 8, 9):
    freq[d] -= 1

m = 0
for i in range(1, 10):
    for _ in range(freq[i]):
        m = (10 * m + i) % 7

suf = ''
for p in list(mod.values()):
    cur = int(str(m) + str(p))
    if cur % 7 == 0:
        suf = str(p)
        break

ans = ''
for i in range(1, 10):
    ans += str(i) * freq[i]

ans += suf
ans += '0' * freq[0]

print(ans)
