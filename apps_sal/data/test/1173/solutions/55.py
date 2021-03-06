from collections import deque
import sys
readline = sys.stdin.readline
N = int(readline())
ALL = N * (N - 1) // 2
player = [None] * N
for i in range(N):
    player[i] = deque(list(map(lambda x: int(x) - 1, readline().split())))
q = set(range(N))
day = 0
while q:
    day += 1
    nextday = set()
    checked = set()
    for p in q:
        if p in checked:
            continue
        if len(player[p]) == 0:
            continue
        op = player[p][0]
        if op in checked:
            continue
        if player[op][0] == p:
            player[p].popleft()
            player[op].popleft()
            checked.add(op)
            checked.add(p)
            if player[p]:
                nextday.add(p)
            if player[op]:
                nextday.add(op)
    q = nextday
for p in player:
    if len(p) > 0:
        print(-1)
        break
else:
    print(day)
