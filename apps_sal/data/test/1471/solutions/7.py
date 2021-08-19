from collections import deque
n = int(input())
col = [-1] * n
e = [[[], []] for i in range(n)]
for i in range(n - 1):
    (u, v, w) = map(int, input().split())
    u -= 1
    v -= 1
    w %= 2
    e[u][w].append(v)
    e[v][w].append(u)
col[0] = 1
dq = deque([])
dq.append(0)
while dq:
    a = dq.pop()
    b = col[a]
    for i in range(2):
        for ne in e[a][i]:
            if col[ne] == -1:
                col[ne] = b ^ i
                dq.appendleft(ne)
print(*col, sep='\n')
