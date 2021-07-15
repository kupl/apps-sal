from collections import deque

N, Q = list(map(int, input().split()))
tree = [set() for _ in range(N+1)]

for i in range(N - 1):
    n1, n2 = list(map(int, input().split()))
    tree[n1].add(n2)
    tree[n2].add(n1)

scores = [0]*(N+1)
for _ in range(Q):
    p, x = list(map(int, input().split()))
    scores[p] += x

q = deque()
q.append(1)
checked = [False]*(N+1)
while q:
    v = q.pop()
    checked[v] = True
    s = scores[v]
    for k in tree[v]:
        if checked[k]:
            continue
        scores[k] += s
        q.append(k)

print((*scores[1:]))

