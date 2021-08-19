from collections import deque
(n, m) = list(map(int, input().split()))
adj_list = [[] for i in range(n)]
for i in range(m):
    (_, __) = list(map(int, input().split()))
    _ -= 1
    __ -= 1
    adj_list[_].append(__)
    adj_list[__].append(_)
distance = [None for i in range(n)]
updated_from = [None for i in range(n)]
newly_visited = deque([0])
distance[0] = 0
while len(newly_visited) > 0:
    now = newly_visited.popleft()
    for i in adj_list[now]:
        if distance[i] is not None:
            continue
        newly_visited.append(i)
        distance[i] = distance[now] + 1
        updated_from[i] = now
'\nprint(distance)\n\nfor i in range(n):\n  # i から 0 に行く経路を求める\n  now = i\n  path = [now]\n  while now != 0:\n    now = updated_from[now]\n    path.append(now)\n  print(i, path) \n'
print('Yes')
for i in range(1, n):
    print(updated_from[i] + 1)
