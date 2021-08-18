from heapq import heappop, heappush
t = int(input())
for test in range(t):
    n, m = (list(map(int, input().split())))
    print(n, 2 * n)
