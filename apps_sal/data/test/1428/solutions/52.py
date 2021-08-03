from collections import defaultdict

n, c = map(int, input().split())
d_s = [list(map(int, input().split())) for _ in range(c)]
c_s = [list(map(int, input().split())) for _ in range(n)]
zot = [defaultdict(int) for _ in range(3)]
for i in range(n):
    for j in range(n):
        zot[(i + j) % 3][c_s[i][j] - 1] += 1


change = [[], [], []]
for i in range(3):
    for j in range(c):
        cnt = 0
        for num, cnt2 in zot[i].items():
            cnt += d_s[num][j] * cnt2
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
