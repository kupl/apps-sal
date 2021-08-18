from collections import deque
import sys
sys.setrecursionlimit(1000000)

N, K = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()

ans = 0
for i in range(K):
    ans += data[i]

print(ans)
