from collections import deque

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

G = [[] for _ in range(n)]
for _ in range(m):
    c, d = map(lambda x: int(x) - 1, input().split())
    G[c].append(d)
    G[d].append(c)

seen = [False] * n
que = deque()

for i in range(n):
    if not seen[i]:
        que.append(i)
        a, b = 0, 0

        while que:
            v = que.pop()
            a += A[v]
            b += B[v]
            seen[v] = True
            for nv in G[v]:
                if not seen[nv]:
                    que.append(nv)
                    seen[nv] = True
        if a != b:
            print("No")
            return
print("Yes")
