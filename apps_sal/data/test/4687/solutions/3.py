from sys import stdin
input = stdin.readline
 
from itertools import accumulate
from bisect import bisect_left
 
N, K = map(int, input().split())
 
memo = [0] * 100010
for _ in range(N):
    a, b = map(int, input().split())
    memo[a] += b
 
print(bisect_left(list(accumulate(memo)), K))
