N = int(input())

X = [[] for _ in range(10**5)]
Y = [[] for _ in range(10**5)]

P = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

for i in range(N):
    x, y = P[i]
    X[x].append(y)
    Y[y].append(x)

x_used = [0 for _ in range(10**5)]
y_used = [0 for _ in range(10**5)]
res = 0

for i in range(10**5):
    if x_used[i]:
        continue
    stack = [(0, i)]
    x_cnt = 1
    x_used[i] = 1
    y_cnt = 0
    edge = 0
    while stack:
        axis, node = stack.pop()
        if axis == 0:
            for adj in X[node]:
                edge += 1
                if y_used[adj]:
                    continue
                y_cnt += 1
                y_used[adj] = 1
                stack.append((1, adj))
        else:
            for adj in Y[node]:
                if x_used[adj]:
                    continue
                x_cnt += 1
                x_used[adj] = 1
                stack.append((0, adj))
    res += x_cnt * y_cnt - edge

print(res)
