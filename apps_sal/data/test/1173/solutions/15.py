from collections import deque
import sys
N = int(input())
match = []
for i in range(N):
    a = list(map(int, input().split()))
    match.append(a)
day = [0] * N
count = [0] * N
q = deque(range(N))
while q:
    p = q.popleft()
    if count[p - 1] < N - 1:
        enemy = match[p - 1][count[p - 1]]
        if p == match[enemy - 1][count[enemy - 1]]:
            today = max(day[p - 1], day[enemy - 1]) + 1
            day[p - 1] = today
            day[enemy - 1] = today
            count[p - 1] += 1
            count[enemy - 1] += 1
            q.append(p)
            q.append(enemy)
if min(count) != N - 1:
    print(-1)
else:
    print(max(day))
