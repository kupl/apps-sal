import sys
import math
import fractions
from collections import defaultdict
from functools import reduce
stdin = sys.stdin


def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


INF = 10**18
mod = 10**9 + 7
N = int(input())
A = nl()
ans = 0
min_bai = 1
for i in range(N):
    min_bai = min_bai * A[i] // fractions.gcd(min_bai, A[i])


for i in range(N):
    ans += min_bai // A[i]

print((ans % mod))
