N,D,A = list(map(int,input().split()))
enemies = [list(map(int,input().split())) for _ in range(N)]
enemies.sort(key=lambda x:x[0])
ans = 0
from collections import deque
damage = deque()
dmg = 0
for x,h in enemies:
    if len(damage) == 0:
        bomb = -(-h//A)
        damage.append([x+2*D,bomb])
        dmg += bomb*A
        ans += bomb
    else:
        while len(damage) > 0:
            d,bomb = damage.popleft()
            if x > d:
                dmg -= bomb*A
            else:
                damage.appendleft([d,bomb])
                break
        if h > dmg:
            bomb = -(-(h-dmg)//A)
            dmg += bomb*A
            damage.append([x+2*D,bomb])
            ans += bomb

print(ans)

