(n, m) = map(int, input().split())
table = [[0] * (m + 2)]
for i in range(n):
    table.append([0])
    s = input()
    for j in range(m):
        table[i + 1].append(2 if s[j] == '*' else 0)
    table[i + 1].append(0)
table.append([0] * (m + 2))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if table[i][j] == 0:
            continue
        able = True
        size = 0
        while able:
            size += 1
            for k in range(4):
                if table[i + dx[k] * size][j + dy[k] * size] == 0:
                    able = False
        size -= 1
        if size > 0:
            table[i][j] = 1
            for k in range(1, size + 1):
                for q in range(4):
                    table[i + dx[q] * k][j + dy[q] * k] = 1
            answer.append([i, j, size])
Ok = True
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if table[i][j] == 2:
            Ok = False
if not Ok:
    print(-1)
else:
    print(len(answer))
    for i in answer:
        print(*i)
