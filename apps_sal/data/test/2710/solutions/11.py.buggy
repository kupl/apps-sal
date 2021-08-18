from collections import deque
import sys

n, m = input().split(' ')
n, m = int(n), int(m)

starts = [int(x) for x in input().split(' ')]
ends = [int(x) for x in input().split(' ')]
num_soldiers = sum(ends)
if sum(starts) != sum(ends):
    print("NO")
    return
# 0 for s, 1 for t, 2 + i for starts, 2 + n + i for ends
f_size = 2 + 2 * n
flow_matrix = [[0] * f_size for _ in range(f_size)]
edge_list = [[] for _ in range(f_size)]


def get_index(i, is_start):
    if is_start:
        return 2 + i
    else:
        return 2 + n + i


for i in range(n):
    flow_matrix[0][get_index(i, True)] = starts[i]
    flow_matrix[get_index(i, False)][1] = ends[i]
    flow_matrix[get_index(i, True)][get_index(i, False)] = num_soldiers

for i in range(m):
    ends = input().split(' ')
    a, b = int(ends[0]), int(ends[1])
    a -= 1
    b -= 1
    flow_matrix[get_index(a, True)][get_index(b, False)] = num_soldiers
    flow_matrix[get_index(b, True)][get_index(a, False)] = num_soldiers

flow_matrix_copy = [x.copy() for x in flow_matrix]
for i in range(f_size):
    for j in range(f_size):
        if flow_matrix[i][j] != 0 or flow_matrix[j][i] != 0:
            edge_list[i].append(j)


def run_bfs(m):
    parent = [None for _ in range(len(m))]
    flow_from_s = [None for _ in range(len(m))]
    q = deque([])
    q.append(0)
    parent[0] = 0
    flow_from_s[0] = 2**20

    found_target = False
    t = 1
    while len(q) > 0 and not found_target:
        front = q.popleft()
        for neighbor in edge_list[front]:
            if flow_matrix[front][neighbor] > 0 and parent[neighbor] is None:
                parent[neighbor] = front
                flow_from_s[neighbor] = min(flow_from_s[front], flow_matrix[front][neighbor])
                q.append(neighbor)
                if neighbor == t:
                    found_target = True
                    break

    if not found_target:
        return 0
    cur = t
    flow = flow_from_s[t]
    while parent[cur] != cur:
        prev = parent[cur]
        flow_matrix[prev][cur] -= flow
        flow_matrix[cur][prev] += flow
        cur = prev
    return flow


def run_flow(m):
    total_flow = 0
    while True:
        flow = run_bfs(m)
        total_flow += flow
        if flow == 0:
            break
    return total_flow


if run_flow(flow_matrix) == num_soldiers:
    print("YES")
    for i in range(n):
        for j in range(n):
            num_along = flow_matrix_copy[get_index(i, True)][get_index(j, False)] - flow_matrix[get_index(i, True)][get_index(j, False)]
            print(str(num_along), end=' ')
        print('')
else:
    print("NO")
