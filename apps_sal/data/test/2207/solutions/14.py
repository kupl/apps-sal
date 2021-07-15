n, m = list(map(int, input().split()))
a = [input() for _ in range(n)]
used = [[False] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if not used[i][j] and a[i][j] == "B":
            ans += 1
            q = [(i, j)]
            used[i][j] = True
            head = 0
            while head < len(q):
                x, y = q[head]
                head += 1
                for d in range(4):
                    xx = x + (1 if d == 0 else -1 if d == 1 else 0)
                    yy = y + (1 if d == 2 else -1 if d == 3 else 0)
                    if 0 <= xx < n and 0 <= yy < m and not used[xx][yy] and a[xx][yy] == "B":
                        used[xx][yy] = True
                        q.append((xx, yy))
print(ans)

