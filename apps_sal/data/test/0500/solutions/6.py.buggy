from collections import deque

n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
gr = [[] for i in range(n)]

for i in range(n - 1):
    a, b = [int(i) for i in input().split()]
    a -= 1
    b -= 1
    gr[a].append(b)
    gr[b].append(a)
for i in range(n):
    if len(gr[i]) > 4:
        print("NO")
        return
print("YES")
d = deque()
d.append((0, 10 ** 18 // 2, 10 ** 18 // 2, -1, -1, 50))
ans = [0] * n
while len(d) > 0:
    v = d[0][0]
    x = d[0][1]
    y = d[0][2]
    ans[v] = (d[0][1], d[0][2])
    p = d[0][4]
    dr = d[0][3]
    pw = d[0][5]
    d.popleft()
    if p != -1:
        gr[v].pop(gr[v].index(p))
    cur = 0
    for i in range(4):
        if i == dr:
            continue
        if cur == len(gr[v]):
            break
        ngh = gr[v][cur]
        d.append((ngh, x + 2 ** pw * dx[i], y + 2 ** pw * dy[i], (i + 2) % 4, v, pw - 1))
        cur += 1
for i in ans:
    print(*i)
