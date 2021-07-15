import heapq
import math

import sys
input = sys.stdin.readline

def li():return [int(i) for i in input().rstrip('\n').split()]
def value():return int(input())

n,k = li()
a = li()

curr = []
currd = {}
currd2 = {}
for i in range(n):
    if a[i] not in currd2:
        if len(curr) == k:
            
            currd2.pop(currd.pop(heapq.heappop(curr)))
        heapq.heappush(curr,i)
        currd[i] = a[i]
        currd2[a[i]] = i
curr.sort(reverse = 1)
ans = []
for i in curr:
    ans.append(currd[i])
print(len(ans))
print(*ans)
