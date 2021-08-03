from collections import deque
from math import ceil

# n个怪物，d杀伤半径，a杀伤值
n, d, a = map(int, input().split())

ms = [map(int, input().split()) for i in range(n)]
ms = sorted([(pos, ceil(hp / a)) for pos, hp in ms])

bombs = deque()

ans = 0
valid_bomb = 0
for pos, hp in ms:
    # 查看队列里的bomb是否对当前怪物有效
    while bombs and bombs[0][0] < pos:
        bomb_border, bomb_cnt = bombs.popleft()
        valid_bomb -= bomb_cnt

    # 还需新加多少bomb才能灭掉当前怪物
    bomb_cnt = max(0, hp - valid_bomb)
    valid_bomb += bomb_cnt
    ans += bomb_cnt

    # 新加的bomb放入队列
    if bomb_cnt > 0:
        bombs.append([pos + d * 2, bomb_cnt])

print(ans)
