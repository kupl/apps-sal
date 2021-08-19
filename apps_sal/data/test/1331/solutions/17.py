# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import math
import heapq
from itertools import accumulate

#N = int(input())

#s = input()
N, M, K = [int(x) for x in stdin.readline().split()]

arr = [int(x) for x in stdin.readline().split()]

freq = [0] * (1000000)

for num in arr:
    freq[num - 1] += 1

s = 0
res = 0
for i in range(1000000):
    if i >= M:
        s -= freq[i - M]

    s += freq[i]
    # print(s)
    if s >= K:
        res += (s - K + 1)
        freq[i] -= (s - K + 1)
        s -= (s - K + 1)

print(res)
