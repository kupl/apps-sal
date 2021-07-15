from collections import deque

N = int(input())
ki = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    ki[u-1].append([v-1, w])
    ki[v-1].append([u-1, w])
f = [False]*N
f[0] = True
c = [0]*N

q = deque([0])
while q:
    now = q.popleft()
    for nxt, w in ki[now]:
        if f[nxt]:
            continue
        if w&1:
            c[nxt] = c[now]^1
        else:
            c[nxt] = c[now]
        q.append(nxt)
        f[nxt] = True


for a in c:
    print(a)
