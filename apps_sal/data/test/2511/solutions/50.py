from collections import deque
(n, k) = map(int, input().split())
inf = pow(10, 9) + 7
tree = [[] for _ in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
not_yet = deque(tree[0])
already = [False] * n
already[0] = True
ans = k
key = k - 1
for v in tree[0]:
    already[v] = True
    ans *= key
    ans %= inf
    key -= 1
while not_yet:
    key = not_yet.popleft()
    for v in range(k - 2, k - 1 - len(tree[key]), -1):
        ans *= v
        ans %= inf
    for value in tree[key]:
        if already[value]:
            continue
        not_yet.append(value)
        already[value] = True
print(ans)
