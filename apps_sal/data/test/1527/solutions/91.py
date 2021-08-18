from collections import deque
h, w = map(int, input().split())
ma = [["
for i in range(h):
    tmp = list(input())
    for j in range(w):
        ma[i + 1][j + 1] = tmp[j]
ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if ma[i][j] == "
            continue
        elif ma[i][j] == ".":
            p = [[-1 for _ in range(w + 2)] for _ in range(h + 2)]
            p[i][j] = 0
            q = deque()
            q.append([i, j])
            while q:
                y, x = q.popleft()
                if ma[y + 1][x] == "." and p[y + 1][x] == -1:
                    p[y + 1][x] = p[y][x] + 1
                    q.append([y + 1, x])
                if ma[y - 1][x] == "." and p[y - 1][x] == -1:
                    p[y - 1][x] = p[y][x] + 1
                    q.append([y - 1, x])
                if ma[y][x + 1] == "." and p[y][x + 1] == -1:
                    p[y][x + 1] = p[y][x] + 1
                    q.append([y, x + 1])
                if ma[y][x - 1] == "." and p[y][x - 1] == -1:
                    p[y][x - 1] = p[y][x] + 1
                    q.append([y, x - 1])
            for l in range(1, h + 1):
                ans = max(ans, max(p[l]))
print(ans)
