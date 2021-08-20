import _heapq
inf = float('inf')


def prim():
    color = ['white' for _ in range(n + 1)]
    D = [inf for _ in range(n + 1)]
    M = [[] for _ in range(n + 1)]
    for (u, v, w) in UVW:
        M[u].append([w, v])
        M[v].append([w, u])
    queue = [[0, 1]]
    _heapq.heapify(queue)
    color[1] = 'gray'
    D[1] = 1
    while len(queue) > 0:
        num = _heapq.heappop(queue)[1]
        if color[num] == 'black':
            continue
        color[num] = 'black'
        for (i, j) in M[num]:
            if D[j] > i and color[j] != 'black':
                if i % 2 == 0:
                    D[j] = D[num]
                else:
                    D[j] = -D[num]
                color[j] = 'gray'
                _heapq.heappush(queue, [i, j])
    return D[1:]


n = int(input())
UVW = [list(map(int, input().split())) for _ in range(n - 1)]
for i in prim():
    if i == 1:
        print(i)
    else:
        print(0)
