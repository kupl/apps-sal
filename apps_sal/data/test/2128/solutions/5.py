import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


def read():
    return list(map(int, input().split()))


def write(*args, sep='\n'):
    for i in args:
        sys.stdout.write('{}{}'.format(i, sep))


INF = float('inf')
MOD = 998244353
YES = 'YES'
NO = 'NO'
n = int(input())
p = [0] + read()
p = list(map(lambda x: x * pow(100, MOD - 2, MOD) % MOD, p))
A = [0] * (n + 2)
for i in range(2, n + 2):
    A[i] = (A[i - 1] - 1) * pow(p[i - 1], MOD - 2, MOD) % MOD
print((-A[-1] + MOD) % MOD)
