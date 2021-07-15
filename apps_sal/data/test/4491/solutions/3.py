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
A1 = LI()
A2 = LI()

if N == 1:
    print(A1[0]+A2[0])
    return

ans = 0
for i in range(N):
    ans = max(ans, sum(A1[:i])+sum(A2[i-1:]))


# A1n = np.zeros(N,dtype='int')
# A1n = np.array(A1)
# A2n = np.zeros(N,dtype='int')
# A2n = np.array(A2)

# A1_cum = np.zeros(N,dtype='int')
# A2_cum = np.zeros(N,dtype='int')
# A1_cum[1:] = A1n[1:].cumsum()
# A2_cum[1:] = A2n[:-1].cumsum()
# # print(A1_cum)
# # print(A2_cum)

# # 下に降りる最初の位置
# start = N - 2
# for i in range(N-1):
#     if A1_cum[N-1] - A1_cum[i] < A2_cum[N-1] - A2_cum[i]:
#         start = i
#         break

# ans = A1n[0] + A2n[-1] + A1_cum[start] + (A2_cum[-1] - A2_cum[start])

# # ans = sum(A1) + sum(A2) - min(A1[-1],A2[0]+A2[1])

print(ans)
