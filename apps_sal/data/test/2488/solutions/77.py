n, d, a = map(int, input().split())
xh = []
for _ in range(n):
    x, h = map(int, input().split())
    h = (h - 1) // a + 1
    xh.append([x, h])
xh.sort()
damage = xh[0][1]
ans = damage
damage_lst = [[xh[0][0] + d * 2, damage]]
pos = 0
for i, (x, h) in enumerate(xh[1:], start = 1):
    while x > damage_lst[pos][0]:
        damage -= damage_lst[pos][1]
        pos += 1
        if pos == i:
            break
    damage_tmp = max(h - damage, 0)
    ans += damage_tmp
    damage += damage_tmp
    damage_lst.append([x + d * 2, damage_tmp])
print(ans)
