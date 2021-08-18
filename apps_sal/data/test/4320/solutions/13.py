from math import sqrt, factorial, gcd, log2, inf, ceil
from math import factorial as f
from itertools import permutations
from heapq import heapify, heappush, heappop
from sys import stdin, stdout
import heapq
from collections import defaultdict
from bisect import bisect_left
from bisect import bisect_right
from queue import PriorityQueue
import random
import sys
from sys import stdin
from collections import deque
mod = 10**9 + 7
def input(): return sys.stdin.readline().rstrip()


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,
                      p - 2, p)) % p


t = int(input())

for _ in range(t):

    n = int(input())
    ans = -1
    for i in range(2, 100):
        if n % (2**i - 1) == 0:
            ans = (n // (2**i - 1))
            break

    print(ans)
