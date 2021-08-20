from collections import deque
import sys
input = sys.stdin.readline


def put():
    return list(map(int, input().split()))


def bfs_(main, co, flag):
    curr = main if flag else co
    while curr:
        x = curr.popleft()
        for y in graph[x]:
            inedge[y] -= 1
            if inedge[y] == 0:
                if is_co[y]:
                    co.append(y)
                else:
                    main.append(y)
    return (main, co)


def bfs():
    (main, co, ans) = (deque(), deque(), 0)
    for i in range(n):
        if inedge[i] == 0:
            if is_co[i]:
                co.append(i)
            else:
                main.append(i)
    while main or co:
        (main, co) = bfs_(main, co, True)
        if co:
            ans += 1
        (main, co) = bfs_(main, co, False)
    return ans


(n, m) = put()
is_co = list(put())
graph = [[] for i in range(n)]
(inedge, vis) = ([0] * n, [0] * n)
for _ in range(m):
    (x, y) = put()
    graph[y].append(x)
    inedge[x] += 1
print(bfs())
