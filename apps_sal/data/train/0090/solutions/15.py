from math import inf, ceil
from heapq import *
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    crr = [arr[i] for i in range(n) if not brr[i]]
    crr.sort(reverse=True)
    ind = 0
    for i in range(n):
        if not brr[i]:
            arr[i] = crr[ind]
            ind += 1
    print(*arr)
