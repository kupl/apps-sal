from _collections import deque
n, m = list(map(int, input().split()))
edg = [[] for i in range(n + 1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    edg[a].append(b)
    edg[b].append(a)
dep = [-1] * (n + 1)
dep[1] = 0
data = deque([1])
while len(data) > 0:
    p = data.popleft()
    for i in edg[p]:
        if dep[i] == -1:
            dep[i] = dep[p] + 1
            data.append(i)
print(("POSSIBLE" if dep[n] == 2 else "IMPOSSIBLE"))
