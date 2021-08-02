import bisect

N, D, A = map(int, input().split())

monsters = []
for i in range(N):
    X, H = map(int, input().split())
    monsters.append([X, H])

monsters = sorted(monsters)

id = 0
ans = 0

damage = [0 for i in range(N)]

while id < N:
    if id > 0:
        damage[id] += damage[id - 1]
    nowX, nowH = monsters[id][0], monsters[id][1]
    nowH -= damage[id]

    if nowH > 0:
        damage[id] += A * ((nowH + A - 1) // A)

        right = bisect.bisect_left(monsters, [nowX + 2 * D + 1, 0])
        if right < N:
            damage[right] -= A * ((nowH + A - 1) // A)

        ans += (nowH + A - 1) // A

    id += 1

print(ans)
