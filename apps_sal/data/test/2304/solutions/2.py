from collections import deque


n, m = map(int, input().split())
rels = [None] + [[] for _ in range(n)]
for _ in range(m):
    l, r, d = map(int, input().split())
    rels[l].append((r, d))
    rels[r].append((l, -d))

x = [None] + [None] * n
i = 0
while i < n:
    i += 1
    if x[i] is not None:
        continue

    q = deque()
    x[i] = 0
    q.append(i)
    while q:
        x1 = q.popleft()
        for x2, d in rels[x1]:
            if x[x1] is not None and x[x2] is not None:
                if x[x2] - x[x1] != d:
                    print('No')
                    return
                continue
            if x[x1] is not None and x[x2] is None:
                x[x2] = x[x1] + d
                q.append(x2)
            elif x[x1] is None and x[x2] is not None:
                x[x1] = x[x2] - d
                q.append(x1)

print('Yes')
