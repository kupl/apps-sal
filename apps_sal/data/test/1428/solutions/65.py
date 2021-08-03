n, c = map(int, input().split())
d_s = [list(map(int, input().split())) for _ in range(c)]
c_s = [list(map(int, input().split())) for _ in range(n)]
zot = [[], [], []]
for i in range(n):
    for j in range(n):
        zot[(i + j) % 3].append(c_s[i][j] - 1)

change = [[], [], []]
for i in range(3):
    for j in range(c):
        cnt = 0
        for num in zot[i]:
            cnt += d_s[num][j]
        change[i].append((cnt, j))
    change[i].sort()

ans = 10 ** 10
for z, i in change[0][:3]:
    for o, j in change[1][:3]:
        if i == j:
            continue
        for t, k in change[2][:3]:
            if k == i or k == j:
                continue
            ans = min(ans, z + o + t)

print(ans)
