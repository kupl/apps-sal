import math
import sys
import os
from operator import mul
import numpy as np

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
ans = N

Sn = np.array(S)
S_cum = np.zeros(N+1,dtype='int')
S_cum[1:] = np.cumsum(Sn=='W')

Snr=np.flip(Sn, 0)
S_cumr = np.zeros(N+1,dtype='int')
S_cumr[1:] = np.cumsum(Snr=='E')

# print(S_cum)
# print(S_cumr)

for i in range(N):
    attention = S_cum[i] + S_cumr[N-(i+1)]
    # print(attention)
    ans = min(ans, attention)

print(ans)
