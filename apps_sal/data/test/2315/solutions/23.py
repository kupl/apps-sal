# alpha = "abcdefghijklmnopqrstuvwxyz"
t = int(input())
from heapq import heappop, heappush
for test in range(t):
    # n = int(input())
    n,m = (list(map(int, input().split())))
    print(n, 2*n)

