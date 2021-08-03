import math
from collections import deque

n, d, a = list(map(int, input().split()))
xh = [list(map(int, input().split())) for _ in range(n)]
xh.sort(key=lambda x: x[0])
xh = deque(xh)

xh_field = deque()

cnt = 0
now_damage = 0
while xh:
    pos, hp = xh.popleft()
    if xh_field:
        while (xh_field and xh_field[0][0] < pos):
            now_damage -= a * xh_field[0][1]
            xh_field.popleft()
    if hp <= now_damage:
        pass
    elif hp > now_damage:
        atk_cnt = math.ceil((hp - now_damage) / a)
        cnt += atk_cnt
        now_damage += atk_cnt * a
        xh_field.append((2 * d + pos, atk_cnt))
print(cnt)
