n = int(input())
graph = [[] for i in range(n + 1)]
for _ in range(n - 1):
    (i, j) = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
mod = 10 ** 9 + 7
start = 1
stack = [1]
s_dist = [0] + [0] + [10 ** 9] * (n - 1)
while stack:
    x = stack.pop()
    for y in graph[x]:
        if s_dist[y] > s_dist[x] + 1:
            s_dist[y] = s_dist[x] + 1
            stack.append(y)
maxdist = max(s_dist)
black = s_dist.index(maxdist)
b_dist = [10 ** 9] * (n + 1)
b_dist[0] = 0
b_dist[black] = 0
stack = [black]
while stack:
    x = stack.pop()
    for y in graph[x]:
        if b_dist[y] > b_dist[x] + 1:
            b_dist[y] = b_dist[x] + 1
            stack.append(y)
maxdist = max(b_dist)
white = b_dist.index(maxdist)
w_dist = [10 ** 9] * (n + 1)
w_dist[0] = 0
w_dist[white] = 0
stack = [white]
while stack:
    x = stack.pop()
    for y in graph[x]:
        if w_dist[y] > w_dist[x] + 1:
            w_dist[y] = w_dist[x] + 1
            stack.append(y)
mindls = [0] * n
maxdls = [0] * n
for i in range(1, n + 1):
    if i in (white, black):
        continue
    mindls[min(w_dist[i], b_dist[i])] += 1
    maxdls[max(w_dist[i], b_dist[i])] += 1
ans = pow(2, n - 1, mod) * maxdist % mod
number = 0
for i in range(1, maxdist + 1):
    if i == maxdist and maxdls[i] == 0:
        continue
    maxdls[i] += maxdls[i - 1]
    if i < maxdist and mindls[i + 1]:
        continue
    ans += (pow(2, maxdls[i], mod) - number) * i * 2
    ans %= mod
    number = pow(2, maxdls[i], mod)
print(ans)
