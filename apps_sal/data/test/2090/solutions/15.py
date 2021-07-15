import sys
input = sys.stdin.readline
import heapq  
N, K = map(int, input().split())
X = [[0, 0] for _ in range(N)]
for i in range(N):
    t, b = map(int, input().split())
    X[i][0] = t
    X[i][1] = b
X = sorted(X, key = lambda x: -x[1])

a = []
s = 0
ma = 0
for i in range(N):
    heapq.heappush(a, X[i][0])
    s += X[i][0]
    if i >= K:
        s -= heapq.heappop(a)
    ma = max(ma, s * X[i][1])

print(ma)
