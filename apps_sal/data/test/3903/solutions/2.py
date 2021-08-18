from collections import deque
n, m = input().split()
n = int(n)
m = int(m)


def idx(i, j):
    return i * m + j


max = n * m * 2
graph = ""
virtDist = [[], [], []]
virtVertex = [deque(), deque(), deque()]
virtNodesDst = [max, max, max]
code = ord("1")
for i in range(0, n):
    s = input()
    graph += s
    for j in range(0, m):
        virtDist[0].append(max)
        virtDist[1].append(max)
        virtDist[2].append(max)
        indx = ord(s[j]) - code
        if 0 > indx or indx > 2:
            continue
        virtVertex[indx].append((i, j))
        i2 = idx(i, j)
        virtDist[indx][-1] = 0


def bfs01(queue, distance):
    while queue:
        pi, pj = queue.popleft()
        for i, j in [(pi, pj - 1), (pi, pj + 1), (pi - 1, pj), (pi + 1, pj)]:
            indx = idx(i, j)
            if 0 > i or i >= n or 0 > j or j >= m or graph[indx] == '
            continue
            isRoad = graph[indx] == "."
            newDistance = distance[idx(pi, pj)] + (1 if isRoad else 0)
            if distance[indx] > newDistance:
                distance[indx] = newDistance
                if isRoad:
                    queue.append((i, j))
                else:
                    queue.appendleft((i, j))


bfs01(virtVertex[0], virtDist[0])
bfs01(virtVertex[1], virtDist[1])
bfs01(virtVertex[2], virtDist[2])

output = max
for i in range(0, n * m):
    output = min(virtDist[0][i] + virtDist[1][i] + virtDist[2]
                 [i] - (2 if graph[i] == "."else 0), output)

print(output if output < max else -1)
