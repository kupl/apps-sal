from collections import deque, Counter


def main():
    with open(0) as f:
        H, W = map(int, f.readline().split())
        maze = [list(line) for line in f.readlines()]

    rank = [[None] * W for _ in range(H)]
    rank[0][0] = 0
    # bfs
    reserved = deque([(0, 0)])
    while len(reserved) > 0:
        x, y = reserved.popleft()
        for u, v in [(s, t) for s, t in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if 0 <= s < H and 0 <= t < W]:
            if rank[u][v] is not None:
                continue
            if maze[u][v] == '.':
                rank[u][v] = rank[x][y] + 1
                reserved.append((u, v))

    if rank[H - 1][W - 1] is None:
        print(-1)
    else:
        counter = Counter()
        for line in maze:
            counter.update(line)
        print(counter['.'] - rank[H - 1][W - 1] - 1)


main()
