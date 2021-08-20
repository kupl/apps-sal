import sys
inf = float('inf')
sys.setrecursionlimit(1000000)
abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
(mod, MOD) = (1000000007, 998244353)
vow = ['a', 'e', 'i', 'o', 'u']
(dx, dy) = ([-1, 1, 0, 0], [0, 0, 1, -1])


def dfs(start):
    stack = [start]
    ct_vertex = 1
    ct_edges = 0
    while stack:
        x = stack.pop()
        visited[x] = True
        for i in graph[x]:
            ct_edges += 1
            if not visited[i]:
                visited[i] = True
                ct_vertex += 1
                stack.append(i)
    if ct_edges == ct_vertex * (ct_vertex - 1):
        return True
    else:
        return False


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def input():
    return sys.stdin.readline().strip()


(n, m) = get_ints()
graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    (x, y) = get_ints()
    graph[x].append(y)
    graph[y].append(x)
visited = [False] * (n + 1)
flag = 0
for i in range(1, n + 1):
    if not visited[i]:
        if not dfs(i):
            flag = 1
            break
if flag == 0:
    print('YES')
else:
    print('NO')
