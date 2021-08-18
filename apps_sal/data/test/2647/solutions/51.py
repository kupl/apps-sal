from collections import deque
a, b = map(int, input().split())
G = []
white_num = 0
for i in range(a):
    s = list(input())
    white_num += s.count('.')
    G.append(s)


def mazesearch(G, initial_h, initial_w, target_h, target_w):
    '''
    G is for example:
        G = [[1,0,1,1,1,1],
            [1,0,1,0,1,0],
            [1,0,1,0,1,1],
            [1,1,1,0,1,1]]
    '''
    steps = 0
    BLOCKED, ALLOWED = '
    UNVISITED, VISITED = 0, 1
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    if G[initial_h][initial_w] == BLOCKED:
        return -1
    height, width = len(G), len(G[0])
    is_visited = [[UNVISITED for w in range(width)] for h in range(height)]
    is_visited[initial_h][initial_w] = VISITED
    queue = deque([(initial_h, initial_w, steps)])
    while queue:
        h, w, steps = queue.popleft()
        if h == target_h and w == target_w:
            return steps
        for dh, dw in directions:
            new_h = h + dh
            new_w = w + dw
            if not (0 <= new_h < height and 0 <= new_w < width):
                continue
            if G[new_h][new_w] == ALLOWED and is_visited[new_h][new_w] == UNVISITED:
                queue.append((new_h, new_w, steps + 1))
                is_visited[new_h][new_w] = VISITED
    return -1


steps = mazesearch(G, 0, 0, a - 1, b - 1)
if steps == -1:
    print(-1, flush=True)
else:
    print(white_num - steps - 1, flush=True)
