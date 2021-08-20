(n, m) = map(int, input().split())
num = []
used = []
for i in range(n):
    num.append(input())
    used.append([False] * m)
ans = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if num[i][j] == '*':
            d1 = 0
            d2 = 0
            d3 = 0
            d4 = 0
            for x in range(j + 1, m):
                if num[i][x] == '.':
                    d1 = x - j - 1
                    break
            else:
                d1 = m - j - 1
            for x in range(j - 1, -1, -1):
                if num[i][x] == '.':
                    d2 = abs(j - x - 1)
                    break
            else:
                d2 = j
            for y in range(i + 1, n):
                if num[y][j] == '.':
                    d3 = y - i - 1
                    break
            else:
                d3 = n - i - 1
            for y in range(i - 1, -1, -1):
                if num[y][j] == '.':
                    d4 = abs(i - y - 1)
                    break
            else:
                d4 = i
            dist = min(d1, d2, d3, d4)
            if dist != 0:
                ans.append([i + 1, j + 1, dist])
                for x in range(j - dist, j + dist + 1):
                    used[i][x] = True
                for y in range(i - dist, i + dist + 1):
                    used[y][j] = True
fl = True
for i in range(n):
    for j in range(m):
        if num[i][j] == '*' and (not used[i][j]):
            fl = False
if not fl:
    print(-1)
else:
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
