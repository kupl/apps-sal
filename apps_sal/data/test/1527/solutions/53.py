(H, W) = map(int, input().split())
S = []
for i in range(H):
    S.append(input())


def bfs(start):
    already = {}
    queue = []
    counter = 0
    queue.append((start[0], start[1], 0))
    already[start] = True
    max_depth = 0
    while counter < len(queue):
        (y, x, depth) = queue[counter]
        if depth > max_depth:
            max_depth = depth
        for move in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y = y + move[0]
            new_x = x + move[1]
            if new_y >= 0 and new_y < H and (new_x >= 0) and (new_x < W) and (S[new_y][new_x] == '.') and ((new_y, new_x) not in already):
                already[new_y, new_x] = True
                queue.append((new_y, new_x, depth + 1))
        counter += 1
    return max_depth


answer = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        depth = bfs((i, j))
        if answer < depth:
            answer = depth
print(answer)
