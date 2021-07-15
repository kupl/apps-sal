from collections import deque

n, m = list(map(int, input().split()))

s1 = input()
s2 = input()

ok = True

for i in range(n):
    for j in range(m):
        c = [[False for _ in range(m)] for __ in range(n)]
        c[i][j] = True

        q = deque()
        q.append((i, j))

        while len(q) > 0:
            x, y = q.popleft()

            if s1[x] == '>' and y + 1 < m and not c[x][y + 1]:
                c[x][y + 1] = True
                q.append((x, y + 1))
            elif s1[x] == '<' and y - 1 >= 0 and not c[x][y - 1]:
                c[x][y - 1] = True
                q.append((x, y - 1))

            if s2[y] == '^' and x - 1 >= 0 and not c[x - 1][y]:
                c[x - 1][y] = True
                q.append((x - 1, y))
            elif s2[y] == 'v' and x + 1 < n and not c[x + 1][y]:
                c[x + 1][y] = True
                q.append((x + 1, y))

        for a in range(n):
            for b in range(m):
                if not c[a][b]:
                    ok = False

if ok:
    print("YES")
else:
    print("NO")

