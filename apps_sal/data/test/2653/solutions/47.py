from collections import deque
(n, q) = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
count = [0] * n
for _ in range(q):
    (p, cnt) = map(int, input().split())
    count[p - 1] += cnt
stack = deque([[0, 0, -1]])
while stack:
    (num, cnt, pr) = stack.pop()
    count[num] += cnt
    for k in tree[num]:
        if k == pr:
            continue
        stack.append([k, count[num], num])
print(*count)
