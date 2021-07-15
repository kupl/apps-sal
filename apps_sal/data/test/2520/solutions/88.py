from collections import deque
import numpy as np

N, M, K = [int(x) for x in input().split()]

friends = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = [int(x) for x in input().split()]
    friends[A].append(B)
    friends[B].append(A)

block = [[] for _ in range(N + 1)]
for i in range(K):
    C, D = [int(x) for x in input().split()]
    block[C].append(D)
    block[D].append(C)

G = []
check = [False] * (N + 1)
for i in range(1, N + 1):
    if check[i] == False:
        check[i] = True
        g = [i]
        q = deque([i])
        while q:
            j = q.popleft()
            for k in friends[j]:
                if check[k] == False:
                    check[k] = True
                    g.append(k)
                    q.append(k)
        G.append(g)

gr = np.array([0] * (N + 1))
fr = np.array([len(friends[i]) for i in range(N + 1)])
bl = np.array([0] * (N + 1))

for g in G:
    s = set(g)
    for v in g:
        gr[v] = len(g)
        b = set(block[v])
        bl[v] = len(s & b)

ans = gr - fr - bl - np.array([1] * (N + 1))

for i in range(1, N + 1):
    print(ans[i], end='')
    if i == N:
        print('')
    else:
        print(' ', end='')
