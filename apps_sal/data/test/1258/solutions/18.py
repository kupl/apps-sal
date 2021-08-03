from collections import defaultdict

n = int(input())
# q = []
# d = defaultdict(int)
# for i in range(n-2):
#     a = list(map(int,input().split()))
#     d[a[0]] += 1
#     d[a[1]] += 1
#     d[a[2]] += 1
#     q.append(a)
#
# a = list(d.items())
# a.sort(key=lambda x: x[1])
#

graph = [[] for i in range(n + 1)]

for _ in range(n - 2):
    a = list(map(int, input().split()))
    graph[a[0]] += [a[1], a[2]]
    graph[a[1]] += [a[0], a[2]]
    graph[a[2]] += [a[1], a[0]]

for i in range(1, n + 1):
    graph[i] = list(set(graph[i]))

visited = [False for i in range(n + 1)]

ans = []

for i in range(1, n + 1):
    if len(graph[i]) == 2:
        ans.append(i)
        visited[i] = True
        break
# print(ans)
for j in graph[i]:
    if len(graph[j]) == 3:
        ans.append(j)
        visited[j] = True
        break
# print(ans)
for i in range(n - 2):
    for j in graph[ans[i]]:
        if not visited[j]:
            ans.append(j)
            visited[j] = True
            # print(ans)

for i in ans:
    print(i, end=' ')
