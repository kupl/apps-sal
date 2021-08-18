from collections import deque
import sys


def input():
    return sys.stdin.readline()[:-1]


n, m = map(int, input().split())
s = ["." * (m + 2)] + ["." + input() + "." for _ in range(n)] + ["." * (m + 2)]
ok = True
num = 0
n_zero = 0
for i in range(1, n + 1):
    p = s[i].count("#")
    num += p
    if p == 0:
        n_zero += 1

m_zero = 0
for j in range(1, m + 1):
    for i in range(1, n + 1):
        if s[i][j] == "#":
            break
    else:
        m_zero += 1

if n_zero * m_zero == 0 and n_zero + m_zero > 0:
    print(-1)
    return
if num == 0:
    print(0)
    return

for i in range(n + 2):
    already = False
    for j in range(1, m + 2):
        if already and s[i][j] == "#":
            ok = False
            break
        elif s[i][j - 1] == "#" and s[i][j] == ".":
            already = True
    if not ok:
        break

for j in range(m + 2):
    already = False
    for i in range(1, n + 2):
        if already and s[i][j] == "#":
            ok = False
            break
        elif s[i - 1][j] == "#" and s[i][j] == ".":
            already = True
    if not ok:
        break

if not ok:
    print(-1)
    return

cnt = 0
visited = [[False for _ in range(m + 2)] for _ in range(n + 2)]
DI = [1, 0, -1, 0]
DJ = [0, 1, 0, -1]


def bfs(x, y):
    q = deque([x * (m + 2) + y])
    while q:
        l = q.popleft()
        i, j = l // (m + 2), l % (m + 2)
        for di, dj in zip(DI, DJ):
            if s[i + di][j + dj] == "#" and visited[i + di][j + dj] == False:
                visited[i + di][j + dj] = True
                q.append((i + di) * (m + 2) + j + dj)
    return


for i in range(n + 2):
    for j in range(m + 2):
        if s[i][j] == "#" and visited[i][j] == False:
            cnt += 1
            visited[i][j] = True
            bfs(i, j)

print(cnt)
