import math
import sys
import os
from operator import mul
import bisect

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")

N = I()
S = list(_S())
ans = 0

r = []
g = []
b = []

for i,s in enumerate(S):
    if s == 'R':
        r.append(i)
    if s == 'G':
        g.append(i)
    if s == 'B':
        b.append(i)

# j = bisect.bisect_right(<list>,<value>)
# print(r)
# print(g)
# print(b)

# for i in r:
#     for j in g:
#         for k in b:
#             tmp = sorted([i,j,k])
#             if not tmp[1]-tmp[0]==tmp[2]-tmp[1]:
#                 ans += 1

ans = len(r)*len(g)*len(b)

for i in range(N):
    for j in range(i,N):
        k = j + (j-i)
        if k > N-1:
            break
        if S[i]==S[j]:
            continue
        if S[i]==S[k] or S[j]==S[k]:
            continue
        ans -= 1

print(ans)

# R G B
# R B G
# G B R
# G R B
# B G R
# B R G

# i   j   k
#  - != -

# RBRBGRBGGB
# 1122233333
# 0000111233
# 0112223334

# B*3
# G*4

# GB系: (2,4), (4,5)
# RB系: (1,3),

