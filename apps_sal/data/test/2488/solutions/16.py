from collections import deque
from math import ceil

n, d, a = map(int, input().split())

ms = [map(int, input().split()) for i in range(n)]
ms = sorted([(pos, ceil(hp / a)) for pos, hp in ms])

bombs = deque()

ans = 0
valid_bomb = 0
for pos, hp in ms:
    while bombs and bombs[0][0] < pos:
        bomb_border, bomb_cnt = bombs.popleft()
        valid_bomb -= bomb_cnt

    bomb_cnt = max(0, hp - valid_bomb)
    valid_bomb += bomb_cnt
    ans += bomb_cnt

    if bomb_cnt > 0:
        bombs.append([pos + d * 2, bomb_cnt])

print(ans)
