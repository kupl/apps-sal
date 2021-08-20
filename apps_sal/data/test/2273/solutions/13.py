from collections import defaultdict
import sys


def fill(graph, n):
    dp = [[True, True, True] for _ in range(n + 1)]
    l = [-1 for i in range(n + 1)]
    from collections import defaultdict
    vis = defaultdict(int)
    (count1, count2, count3) = (0, 0, 0)
    for i in graph:
        if dp[i][0]:
            (l[i], count1) = (1, count1 + 1)
            vis[i] = 1
            for j in graph[i]:
                dp[j][0] = False
        elif dp[i][1]:
            l[i] = 2
            count2 += 1
            vis[i] = 2
            for j in graph[i]:
                dp[j][1] = False
        elif dp[i][2]:
            l[i] = 3
            count3 += 1
            vis[i] = 3
            for j in graph[i]:
                dp[j][2] = False
        else:
            return [-1]
    if count1 == 0 or count2 == 0 or count3 == 0:
        return [-1]
    if count1 + count2 + count3 != n:
        return [-1]
    if count1 * count2 + count2 * count3 + count1 * count3 != m:
        return [-1]
    l.pop(0)
    for i in l:
        if i == -1:
            return [-1]
    return l


(n, m) = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for i in range(m):
    (a, b) = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)
k = fill(graph, n)
print(*k)
