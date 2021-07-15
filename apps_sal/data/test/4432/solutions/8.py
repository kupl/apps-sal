from sys import stdin, exit
from bisect import *
from heapq import heappush, heappop
from itertools import combinations
from collections import deque
input = stdin.readline
lmi = lambda: list(map(int, input().split()))
mi = lambda: map(int, input().split())
si = lambda: input().strip('\n')
ssi = lambda: input().strip('\n').split()

for _ in range(int(input())):
    n = int(input())
    arr = lmi()
    i = 0
    tmp = []
    ans = 0
    while i < n:
        tmp.append(arr[i])
        i+= 1
        if i >=n or (arr[i] > 0) != (arr[i-1] > 0):
            ans += max(tmp)
            tmp = []
    print(ans)
