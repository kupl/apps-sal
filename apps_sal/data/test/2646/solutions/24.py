from collections import deque


def show_2d_array(array):
    [print(a) for a in array]


N, M = map(int, input().split())

cave = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    cave[a - 1].append(b - 1)
    cave[b - 1].append(a - 1)


# show_2d_array(cave)


def bfs(tree, p):
    seen = [False] * len(tree)
    queue = deque((p,))
    depth = [0] * N
    depth[p] = 0
    current_depth = depth[p]
    while len(queue) > 0:
        # print(queue)
        q = queue.popleft()
        seen[q] = True
        # print(q)
        for v in tree[q]:
            if not seen[v]:
                depth[v] = depth[q] + 1
                queue.append(v)
                seen[v] = True

    return depth


depth = bfs(cave, 0)

# print("depth", depth)

sign = [0] * N
ans = "Yes"
for i in range(1, N):
    this_depth = depth[i]
    found = False
    for j in cave[i]:
        if depth[j] == this_depth - 1:
            sign[i] = j
            found = True
            break
    if not found:
        ans = "No"
        break

"""
for i in range(1, N):
    current = i
    found = False
    while not found:
        next = -1
        for j in cave[current]:
            if depth[j] == depth[current]-1:
                if sign[current] <= 0:
                    next = j
                    sign[current] = next
                    break
                else:
                    next = sign[current]
                    break
        if next < 0:
            ans = "No"
            break

        current = next
        if current == 0:
            found = True
"""

print(ans)
if ans == "Yes":
    [print(s + 1) for s in sign[1:]]
