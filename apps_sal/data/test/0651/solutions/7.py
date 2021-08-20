(r, s) = list(map(int, input().split()))
m = []
for i in range(r):
    m.append(input())
    for j in range(s):
        if m[i][j] == 'S':
            start = (i, j)
se = input()
u = [0, 1, 0, -1]
v = [1, 0, -1, 0]
sol = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                if len(set([a, b, c, d])) < 4:
                    continue
                (x, y) = start
                cnt = 0
                for znak in se:
                    if znak == '0':
                        x += u[a]
                        y += v[a]
                    if znak == '1':
                        x += u[b]
                        y += v[b]
                    if znak == '2':
                        x += u[c]
                        y += v[c]
                    if znak == '3':
                        x += u[d]
                        y += v[d]
                    cnt += 1
                    if x < 0 or y < 0 or x >= r or (y >= s):
                        cnt = -1
                        break
                    if m[x][y] not in ['.', 'S']:
                        break
                if cnt > 0 and m[x][y] == 'E':
                    sol += 1
print(sol)
