# 次に試合したい相手をdequeで管理
# お互いの試合したい相手(dequeの先頭)が一致すれば試合できる
# 次の日のチェック対象は「前日に試合した人」だけ。これをキュー管理

from collections import deque
import sys
readline = sys.stdin.readline

N = int(readline())
ALL = (N * (N - 1)) // 2  # 試合数

player = [None] * N
for i in range(N):
    player[i] = deque(list(map(lambda x: int(x) - 1, readline().split())))

# 明日試合する候補の人
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
        op = player[p][0]  # 次の対戦相手
        if op in checked:
            continue
        if player[op][0] == p:
            # 試合成立
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
