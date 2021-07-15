from collections import deque

N, M, *AB = map(int, open(0).read().split())

E = [[] for _ in range(N + 1)]
for a, b in zip(*[iter(AB)] * 2):
    E[a].append(b)

shortest = N + 1
ans = []
for s in range(1, N + 1):
    D = [-1] * (N + 1)
    P = [-1] * (N + 1)

    D[s] = 0
    Q = deque([s])
    while Q:
        p = Q.popleft()
        for c in E[p]:
            if D[c] < 0:
                D[c] = D[p] + 1
                P[c] = p
                Q.append(c)

    for t in range(1, N + 1):
        if t == s or D[t] < 0:
            continue

        for v in E[t]:
            if v != s:
                continue

            T = [s]
            cur = t
            while cur != s:
                T.append(cur)
                cur = P[cur]

            if shortest > len(T):
                shortest = len(T)
                ans = T

if shortest == N + 1:
    print(-1)
else:
    print(len(ans))
    print("\n".join(map(str, ans)))
