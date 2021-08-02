import sys
import threading


def put():
    return list(map(int, sys.stdin.readline().split()))


def dfs(i, h):
    vis[i] = h
    done[i] = 1
    element.append(i)
    for j in graph[i]:
        if vis[j] != 0 and h - vis[j] >= k:
            ind = element.index(j)
            ans.extend(element[ind:])
            raise ValueError
        elif done[j] == 0:
            dfs(j, h + 1)
    vis[i] = 0
    element.pop()


def solve():
    try:
        for i in range(1, n + 1):
            if done[i] == 0:
                dfs(i, 1)
    except:
        print(len(ans))
        print(*ans)


n, m, k = put()
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = put()
    graph[x].append(y)
    graph[y].append(x)

done, vis = [0] * (n + 1), [0] * (n + 1)
element, ans = [], []


max_recur_size = 10**5 * 2 + 1000
max_stack_size = max_recur_size * 500
sys.setrecursionlimit(max_recur_size)
threading.stack_size(max_stack_size)
thread = threading.Thread(target=solve)
thread.start()
