from collections import deque

n, m = list(map(int, input().split()))
a = [[] for _ in range(n)]

for i in range(m):
    x, y = list(map(int, input().split()))
    a[x - 1].append(y - 1)
    a[y - 1].append(x - 1)

c = [0] * n
que = deque([])
que.append(0)

while len(que) > 0:
    e = que.popleft()
    for i in a[e]:
        if c[i] > 0:
            continue
        c[i] = e + 1
        que.append(i)
print("Yes")
for i in range(1, n):
    print((c[i]))
