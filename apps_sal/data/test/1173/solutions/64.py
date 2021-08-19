from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    line = list([int(x) - 1 for x in input().split()])
    A.append(line)
cnt = [0] * N
recent = [0] * N
Q = deque(list(range(N)))
while Q:
    p1 = Q.popleft()
    if cnt[p1] < N - 1:
        p2 = A[p1][cnt[p1]]
        if cnt[p2] < N - 1:
            if A[p2][cnt[p2]] == p1:
                day = max(recent[p1], recent[p2]) + 1
                recent[p1] = day
                recent[p2] = day
                cnt[p1] += 1
                cnt[p2] += 1
                Q.append(p1)
                Q.append(p2)
if min(cnt) != N - 1:
    print(-1)
else:
    print(max(recent))
