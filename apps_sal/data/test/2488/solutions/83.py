

import collections
n, d, a = list(map(int, input().split()))
enemies = [list(map(int, input().split())) for _ in range(n)]

enemies.sort(key=lambda a: a[0])

d *= 2
total_damage = 0

q = collections.deque()

ans = 0
for i in range(n):
    x = enemies[i][0]
    hp = enemies[i][1]

    while (len(q) and q[0][0] < x):
        total_damage -= q[0][1]
        q.popleft()

    hp -= total_damage
    if hp > 0:
        times = (hp + a - 1) // a
        total_damage += a * times
        ans += times

        q.append((x + d, a * times))

print(ans)
