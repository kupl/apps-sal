from collections import Counter, defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline


def solve():
    n, k = [int(x) for x in input().split()]
    arr = [x for x in input().strip()]
    arr.sort()
    first = arr[:k]
    if first[0] == first[-1]:
        rest = arr[k:]
        if len(Counter(rest)) == 1:
            print(first[0] + rest[0] * math.ceil(len(rest) / k))
        else:
            print(first[0] + ''.join(rest))
    else:
        print(first[-1])


tt = int(input())
for test in range(tt):
    solve()
