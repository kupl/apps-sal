import math
# import sys
# input = sys.stdin.readline
n, m = [int(i) for i in input().split(' ')]
d = [[] for i in range(n)]
done = [False for i in range(n)]


def dfs(visited, i, d):
    visited[i] = True
    done[i] = True
    for j in d[i]:
        if visited[j]:
            return True
        if not done[j]:
            temp = dfs(visited, j, d)
            if temp:
                return True
    visited[i] = False
    return False


edgelist = []
for i in range(m):
    a, b = [int(i) for i in input().split(' ')]
    edgelist.append([a, b])
    d[a - 1].append(b - 1)

ans = 0
visited = [False for i in range(n)]
for i in range(n):
    if dfs(visited, i, d):
        ans = 1
        break
if ans:
    print(2)
    for i in edgelist:
        if i[0] > i[1]:
            print(2, end=' ')
        else:
            print(1, end=' ')
else:
    print(1)
    print(' '.join('1' for i in range(m)))
