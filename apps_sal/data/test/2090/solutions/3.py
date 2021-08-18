import heapq
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, K = list(map(int, input().split()))
songs = [list(map(int, input().split())) for _ in range(N)]

songs = sorted(songs, key=lambda x: x[1], reverse=True)

ans = -float('inf')
S = []
tmpS = 0
for t, v in songs:
    if len(S) < K:
        heapq.heappush(S, t)
        tmpS += t
        minB = v
    else:
        if S[0] <= t:
            tmpS = tmpS - S[0] + t
            heapq.heappop(S)
            heapq.heappush(S, t)
            minB = v
    ans = max(ans, minB * tmpS)
print(ans)
