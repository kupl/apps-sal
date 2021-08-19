# alpha = "abcdefghijklmnopqrstuvwxyz"
from heapq import heappop, heappush
t = int(input())
for test in range(t):
    # n = int(input())
    n, m = (list(map(int, input().split())))
    print(n, 2 * n)
