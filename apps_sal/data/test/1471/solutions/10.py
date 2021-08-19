from collections import deque
n = int(input())
explored = set()
next = [[] for _ in range(n)]
ls = []
for i in range(n - 1):
    (u, v, w) = map(int, input().split())
    ls.append((u - 1, v - 1, w % 2))
    next[u - 1].append((v - 1, w % 2))
    next[v - 1].append((u - 1, w % 2))
ans = [-1] * n
exploring = deque()
next_que = deque([0])
ans[0] = 0
explored.add(0)
while next_que:
    i = next_que.popleft()
    exploring.extend(next[i])
    while exploring:
        (a, b) = exploring.popleft()
        ans[a] = (ans[i] + b) % 2
        list = next[a]
        if a not in explored:
            next_que.append(a)
        explored.add(a)
for i in ans:
    print(i)
