from itertools import accumulate
import heapq
import sys
input = sys.stdin.readline
t = int(input())
for test in range(t):
    n = int(input())
    M = [[] for i in range(n)]
    MCOUNT = [0] * n
    for i in range(n):
        (m, p) = list(map(int, input().split()))
        M[m].append(p)
        MCOUNT[m] += 1
    ACC = list(accumulate(MCOUNT))
    HQ = []
    ANS = 0
    use = 0
    for i in range(n - 1, -1, -1):
        for j in M[i]:
            heapq.heappush(HQ, j)
        while ACC[i - 1] + use < i:
            x = heapq.heappop(HQ)
            ANS += x
            use += 1
    print(ANS)
