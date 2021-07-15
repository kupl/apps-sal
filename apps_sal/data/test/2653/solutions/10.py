from collections import deque
N, Q = list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
counter = [0]*(N+1)
for i in range(N-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)
for i in range(Q):
    p, x = list(map(int, input().split()))
    counter[p] += x
parent = [-1]*(N+1)
d = deque([1])

while d:
    a = d.popleft()
    for b in tree[a]:
        if parent[a] != b:
            parent[b] = a
            counter[b] += counter[a]
            d.append(b)

print((*counter[1:]))

