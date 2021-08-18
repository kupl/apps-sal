from collections import defaultdict
n, m = list(map(int, input().split()))
ad = defaultdict(list)
ans = []
for i in range(m):
    x, y = list(map(int, input().split()))
    ad[x].append(y)
    ad[y].append(x)


def BFS(s):

    visited = [False] * (n + 1)

    queue = []
    k = 0

    queue.append(s)
    visited[s] = True

    while k < len(queue):

        s = queue[k]
        k += 1
        for i in ad[s]:
            if visited[i] == False:
                queue.append(i)
                ans.append((s, i))
                visited[i] = True
    for i in range(n - 1):
        print(ans[i][0], ans[i][1])


m = 0
s = 1
for i in ad:
    if len(ad[i]) > m:
        m = len(ad[i])
        s = i
BFS(s)
