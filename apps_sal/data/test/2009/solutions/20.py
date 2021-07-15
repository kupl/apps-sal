from collections import deque
import sys

n = int(input())
r1, c1 = map(lambda x : int(x) - 1, input().split())
r2, c2 = map(lambda x : int(x) - 1, input().split())

graph = []
components = []
land_components = {}

visited = set()

for i in range(n):
    row = input()
    graph.append(row)

def find_component(r, c):
    q = deque()
    q.append((r, c))
    queued = set()
    queued.add((r, c))
    result = []

    while q:
        cell = q.popleft()
        result.append(cell)

        consider = []

        r, c = cell

        if r > 0 and graph[r - 1][c] == '0':
            consider.append((r - 1, c))
        if c > 0 and graph[r][c - 1] == '0':
            consider.append((r, c - 1))
        if r < n - 1 and graph[r + 1][c] == '0':
            consider.append((r + 1, c))
        if c < n - 1 and graph[r][c + 1] == '0':
            consider.append((r, c + 1))
        for candidate in consider:
            if candidate not in queued:
                q.append(candidate)
                queued.add(candidate)

    return result

comp1 = find_component(r1, c1)
if (r2, c2) in comp1:
    print(0)
    return

comp2 = find_component(r2, c2)

best = None

for tuple1 in comp1:
    for tuple2 in comp2:
        dist = pow(tuple1[0] - tuple2[0], 2) + pow(tuple1[1] - tuple2[1], 2)
        if not best or best > dist:
            best = dist

print(best)
