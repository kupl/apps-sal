from collections import deque


def input2():
    return map(int, input().split())


def input_array():
    return list(map(int, input().split()))


n, m = input2()
g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = input2()
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(1)

check = [0] * (n + 1)
check[1] = 1

ans = [0] * (n + 1)
ans[1] = 1
for _ in range(10**5 + 1):
    if len(q) == 0:
        break
    v = q.popleft()
    for u in g[v]:
        if check[u] == 0:
            check[u] = 1
            ans[u] = v
            q.append(u)
print("Yes")
for i in range(2, n + 1):
    print(ans[i])
