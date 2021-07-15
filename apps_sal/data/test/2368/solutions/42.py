from collections import deque
n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

G = [[] for _ in range(n)]
for i in range(m):
    i,j = map(int, input().split())
    i -= 1
    j -= 1
    G[i].append(j)
    G[j].append(i)

seen = [False] * n
que = deque()

for i in range(n):
    if not seen[i]:
        que.append(i)
        seen[i] = True
        a, b = 0, 0
        while len(que):
            v = que.popleft()
            a += A[v]
            b += B[v]
            for nv in G[v]:
                if not seen[nv]:
                    que.append(nv)
                    seen[nv] = True
        if a != b:
            print("No")
            return

print("Yes")
