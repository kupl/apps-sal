import sys
import math
import itertools
import heapq
import bisect

def solution(n,arr):

    count = {}
    for i,num in enumerate(arr):
        if num in count:
            heapq.heappush(count[num], i)
        else:
            count[num] = [i]

    pq = []
    for num,c in count.items():
        occs = len(c) 
        if occs >= 2:
            heapq.heappush(pq, num)

    while pq:
        num = heapq.heappop(pq)
        if len(count[num]) < 2:
            continue
        i = heapq.heappop(count[num])
        j = heapq.heappop(count[num])
        arr[i] = None
        arr[j] = num * 2
        if num * 2 in count:
            heapq.heappush(count[num*2], j)
            if len(count[num*2]) >= 2:
                heapq.heappush(pq, num*2)
        else:
            count[num * 2] = [j]
        if len(count[num]) >= 2:
            heapq.heappush(pq, num)

    res = [str(ai) for ai in arr if ai != None]
    print(len(res))
    print(' '.join(res))

n = sys.stdin.readline().strip()
arr = list(map(int, sys.stdin.readline().strip().split(' ')))
solution(n,arr)
