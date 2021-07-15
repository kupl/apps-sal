from bisect import bisect_right

n, d, a = list(map(int, input().split()))
lxh = [tuple(map(int, input().split())) for _ in range(n)]

lxh.sort()
lx, lh = [], []
for x, h in lxh:
    lx.append(x)
    lh.append(h)

n_bomb = 0
total_damage = 0
subtract = [0 for _ in range(n + 1)]

for i in range(n):
    total_damage -= subtract[i]

    x = lx[i]
    h = lh[i] - total_damage

    if h > 0:
        n_bomb += -(-h // a)
        damage = -(-h // a) * a
        total_damage += damage

        i_sub = bisect_right(lx, x + 2 * d)
        subtract[i_sub] += damage

print(n_bomb)

