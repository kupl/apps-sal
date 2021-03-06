from queue import Queue
import sys


def input():
    return sys.stdin.readline().strip()


(n, u, v) = map(int, input().split())
(u, v) = (u - 1, v - 1)
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
aoki = [-1 for _ in range(n)]
aoki[v] = 0
todo = Queue()
todo.put(v)
while not todo.empty():
    i = todo.get()
    for j in tree[i]:
        if aoki[j] == -1:
            todo.put(j)
            aoki[j] = aoki[i] + 1
taka = [-1 for _ in range(n)]
taka[u] = 0
todo = Queue()
todo.put(u)
while not todo.empty():
    i = todo.get()
    for j in tree[i]:
        if taka[j] == -1:
            if taka[i] + 1 < aoki[j]:
                todo.put(j)
            taka[j] = taka[i] + 1
ans = 0
for i in range(n):
    if taka[i] != -1:
        if aoki[i] - 1 > ans:
            ans = aoki[i] - 1
print(ans)
