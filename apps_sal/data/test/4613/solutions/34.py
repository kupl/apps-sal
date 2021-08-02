from collections import deque
number, m = list(map(int, input().split()))

h = deque([])

for _ in range(m):
    l = list(map(int, input().split()))
    h.append(l)
count = 0

for i in range(m):
    if i != 0:
        h.append([a1, b1])
    a1, b1 = h.popleft()
    g = [[] for _ in range(number)]
    for a, b in h:

        g[a - 1].append(b)
        g[b - 1].append(a)

    q = deque([a1])
    pre = [0] * number
    pre[a1 - 1] = 1
    while q:
        now = q.popleft()

        for n in g[now - 1]:

            if pre[n - 1] == 0:
                q.append(n)
                pre[n - 1] = 1
            else:
                continue

    if sum(pre) != number:
        count += 1

print(count)
