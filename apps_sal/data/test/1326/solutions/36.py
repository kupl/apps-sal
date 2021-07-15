import math
import sys
import os
from operator import mul
import numpy as np
# import sympy

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
ans = 0

# 足し方の見方を変える。等差数列の和をKまで足す
# 1 + 2 + 3 + 4 +...
#   + 2     + 4 +...
for i in range(1,N+1):
    # Nを超えない整数
    y = N//i
    sum = y*(y+1)*i/2
    ans += sum

print(int(ans))





# 素数 エラトステネス
def seachPrimeNum(N):
   max = int(np.sqrt(N))
   seachList = [i for i in range(2,N+1)]
   primeNum = []
   while seachList[0] <= max:
       primeNum.append(seachList[0])
       tmp = seachList[0]
       seachList = [i for i in seachList if i % tmp != 0]
   primeNum.extend(seachList)
   return primeNum

# 約数
def divisor_count(n):
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1

    return divisors
