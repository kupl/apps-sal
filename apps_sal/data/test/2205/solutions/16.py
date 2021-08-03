import sys
from math import *
from fractions import gcd
def readints(): return list(map(int, input().strip('\n').split()))


n = int(input())
a = list(readints())


# for k in range(1,9):
#     buf=''
#     for i in range(1,9):
#         buf+=str(i%k)+' '
#     print(buf)

P = 0
for p in a:
    P = P ^ p

maxn = 10**6 + 5
prefix = [0] * maxn
for i in range(1, maxn):
    prefix[i] = prefix[i - 1] ^ i


cur = 0
for k in range(1, n + 1):
    base = n // k
    if base % 2 == 1:
        cur = cur ^ prefix[k - 1]
    cur = cur ^ prefix[n % k]


Q = cur ^ P
print(Q)
