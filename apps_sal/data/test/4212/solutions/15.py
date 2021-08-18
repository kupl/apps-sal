from collections import deque
n, m, q = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(q)]
a, b, c, d = [list(i) for i in zip(*l)]
queue = deque([[1]])
ans = 0
while queue:
    x = queue.popleft()
    if len(x) == n:
        s = 0
        for i in range(q):
            if x[b[i] - 1] - x[a[i] - 1] == c[i]:
                s += d[i]
        ans = max(ans, s)
    else:
        for j in range(x[-1], m + 1):
            y = x + [j]
            queue.append(y)
print(ans)
