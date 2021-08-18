from collections import deque
import math

N, D, A = list(map(int, input().split()))
XH = [list(map(int, input().split())) for _ in range(N)]
XH.sort(key=lambda x: x[0])


ans = 0
total_damage = 0
dq = deque()

for x, h in XH:
    while dq and dq[0][1] < x:
        dmg, rng = dq.popleft()
        total_damage -= dmg

    if total_damage < h:
        h -= total_damage
        cnt = math.ceil(h / A)
        ans += cnt
        dmg = cnt * A
        total_damage += dmg
        dq.append((dmg, x + D * 2))

print(ans)
