import math

n, m, s = map(int, input().split())

road = []
for i in range(m):
    u, v, a, b = map(int, input().split())
    road.append([u, v, a, b])

change = []
for i in range(n):
    c, d = map(int, input().split())
    change.append([c, d])

tree = [[] for _ in range(n + 1)]

for i in range(m):
    r = road[i]
    tree[r[0]].append([r[0], r[1], r[2], r[3]])
    tree[r[1]].append([r[1], r[0], r[2], r[3]])

least_cost = [[] for _ in range(n + 1)]
for l in range(n + 1):
    least_cost[l] = [math.inf] * 2501


def insort_queue(q, v):
    len_a = len(q)
    if len_a == 0:
        q.append(v)
        return

    min = 0
    max_1 = len_a

    if max_1 == 1:
        if v[2] > q[0][2]:
            min = 1
        else:
            min = 0
    while max_1 - min > 1:
        mid = (max_1 + min) // 2
        if v[2] > q[mid][2]:
            min = mid
        else:
            max_1 = mid
    index = max_1
    q.insert(index, v)


queue = []


def dijakstra(q):
    while q != []:
        hwd = q.pop(0)

        if least_cost[hwd[0]][hwd[1]] > hwd[2]:
            least_cost[hwd[0]][hwd[1]] = hwd[2]

            for node in tree[hwd[0]]:
                if hwd[1] - node[2] >= 0:
                    insort_queue(q, [node[1], hwd[1] - node[2], hwd[2] + node[3]])
            if hwd[1] + change[hwd[0] - 1][0] <= 500:
                insort_queue(q, [hwd[0], hwd[1] + change[hwd[0] - 1][0], hwd[2] + change[hwd[0] - 1][1]])
    return least_cost


if s > 2500:
    s = 2500
queue.append([1, s, 0])

ans = dijakstra(queue)

for i in range(2, n + 1):
    print(min(ans[i]))
