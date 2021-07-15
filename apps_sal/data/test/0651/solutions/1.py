from itertools import permutations

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

n, m = list(map(int, input().split()))
s = [input() for _ in range(n)]

spos = (0, 0)
for i in range(n):
    for j in range(m):
        if s[i][j] == 'S':
            spos = (j, i)

t = input()

ans = 0
for p in permutations(dirs):
    x, y = spos
    for c in t:
        dr = p[int(c)]
        x += dr[0]
        y += dr[1]
        if not 0 <= x < m or not 0 <= y < n:
            break
        if s[y][x] == '#':
            break
        if s[y][x] == 'E':
            ans += 1
            break

print(ans)

