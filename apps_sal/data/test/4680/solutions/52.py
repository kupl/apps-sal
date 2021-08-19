from sys import stdin, stdout
from time import perf_counter
import sys
sys.setrecursionlimit(10 ** 9)
mod = 10 ** 9 + 7
l = sorted(map(int, input().split()))
print('YES' if l == [5, 5, 7] else 'NO')
