from math import sqrt, factorial, gcd, log2, inf, ceil
from heapq import heapify, heappush, heappop
from sys import stdin, stdout
import heapq
from collections import defaultdict
from bisect import bisect_left
from bisect import bisect_right
from queue import PriorityQueue
import sys
from sys import stdin
from collections import deque
mod = 10**9 + 7
sys.setrecursionlimit(10**5)
def input(): return sys.stdin.readline().rstrip()


n = int(input())

ans = 0

for i in range(2, n + 1):
    ans += i * (n // i - 1)

print(ans * 4)
