from collections import deque
n = int(input())
ab = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ab[a].append([b, i])
que = deque()
que.append(1)
visited = [0] * (n)
ans = [0] * (n - 1)
while que:
    x = que.popleft()
    k = 1
    for j in ab[x]:
        if visited[x - 1] != k:
            ans[j[1]] += k
            visited[j[0] - 1] += k
            k += 1
            que.append(j[0])
        else:
            ans[j[1]] += (k + 1)
            visited[j[0] - 1] += (k + 1)
            k += 2
            que.append(j[0])
print(max(ans))
for l in ans:
    print(l)
