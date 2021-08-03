from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, 0)
B = list(map(int, input().split()))
B.insert(0, 0)
G = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    c, d = map(int, input().split())
    G[c].append(d)
    G[d].append(c)
Col = [-1 for _ in range(N + 1)]
cnt = 0
for i in range(1, N + 1):
    if Col[i] < 0:
        que = deque([i])
        Col[i] = cnt
        while que:
            x = que.popleft()
            for y in G[x]:
                if Col[y] < 0:
                    Col[y] = cnt
                    que.append(y)
        cnt += 1
Mem = {c: [] for c in range(cnt)}
for i in range(1, N + 1):
    Mem[Col[i]].append(i)
flag = 0
for c in Mem:
    c1 = 0
    c2 = 0
    for i in Mem[c]:
        c1 += A[i]
        c2 += B[i]
    if c1 != c2:
        flag = 1
        break
if flag == 0:
    print("Yes")
else:
    print("No")
