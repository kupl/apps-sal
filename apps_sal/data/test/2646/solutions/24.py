from collections import deque


def show_2d_array(array):
    [print(a) for a in array]


(N, M) = map(int, input().split())
cave = [[] for i in range(N)]
for i in range(M):
    (a, b) = map(int, input().split())
    cave[a - 1].append(b - 1)
    cave[b - 1].append(a - 1)


def bfs(tree, p):
    seen = [False] * len(tree)
    queue = deque((p,))
    depth = [0] * N
    depth[p] = 0
    current_depth = depth[p]
    while len(queue) > 0:
        q = queue.popleft()
        seen[q] = True
        for v in tree[q]:
            if not seen[v]:
                depth[v] = depth[q] + 1
                queue.append(v)
                seen[v] = True
    return depth


depth = bfs(cave, 0)
sign = [0] * N
ans = 'Yes'
for i in range(1, N):
    this_depth = depth[i]
    found = False
    for j in cave[i]:
        if depth[j] == this_depth - 1:
            sign[i] = j
            found = True
            break
    if not found:
        ans = 'No'
        break
'\nfor i in range(1, N):\n    current = i\n    found = False\n    while not found:\n        next = -1\n        for j in cave[current]:\n            if depth[j] == depth[current]-1:\n                if sign[current] <= 0:\n                    next = j\n                    sign[current] = next\n                    break\n                else:\n                    next = sign[current]\n                    break\n        if next < 0:\n            ans = "No"\n            break\n\n        current = next\n        if current == 0:\n            found = True\n'
print(ans)
if ans == 'Yes':
    [print(s + 1) for s in sign[1:]]
