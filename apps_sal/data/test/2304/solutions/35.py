from collections import deque

N, M = list(map(int, input().split()))

links = [[] for _ in range(N + 1)]
for _ in range(M):
    L, R, D = list(map(int, input().split()))
    links[L].append((R, D))
    links[R].append((L, -D))

t = [None] * (N + 1)
for i in range(1, N + 1):
    if t[i] is not None:
        continue
    t[i] = 0
    s = deque([i])
    while s:
        j = s.popleft()
        for k, l in links[j]:
            if t[k] is None:
                t[k] = t[j] + l
                s.append(k)
            else:
                if t[k] != t[j] + l:
                    print('No')
                    return
print('Yes')
