from collections import deque
k = int(input())
d = [k] * k
e = [[(0, i * 10 % k), (1, (i + 1) % k)] for i in range(k)]
dq = deque()
dq.append((1, 1))
while dq:
    (c, v) = dq.popleft()
    for (v2nv, nv) in e[v]:
        if v2nv == 0:
            if c < d[nv]:
                d[nv] = c
                dq.appendleft((d[nv], nv))
        elif c + 1 < d[nv]:
            d[nv] = c + 1
            dq.append((d[nv], nv))
print(d[0])
