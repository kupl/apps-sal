import collections

n, k = map(int, input().split())
mod = 10 ** 9 + 7
graph = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
flag = [False for i in range(n + 1)]
flag[1] = True
queue = collections.deque([1])
ans = k
while queue:
    test = queue.popleft()
    temp = [flag[graph[test][i]] for i in range(len(graph[test]))].count(True)
    num = 0
    for i in range(len(graph[test])):
        if flag[graph[test][i]] == True:
            continue
        ans *= (k - temp - num - 1)
        ans %= mod
        num += 1
        queue.append(graph[test][i])
        flag[graph[test][i]] = True
print(ans)
