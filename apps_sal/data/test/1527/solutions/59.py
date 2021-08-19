from collections import deque


def main():
    (row, col) = list(map(int, input().split()))
    S = [list(input()) for _ in range(row)]
    ans = 0
    for r in range(row):
        for c in range(col):
            if S[r][c] == '#':
                continue
            q = deque()
            q.append((r, c))
            dist = [[-1 for _ in range(col)] for _ in range(row)]
            dist[r][c] = 0
            while q:
                (r, c) = q.popleft()
                for (dr, dc) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    (nr, nc) = (r + dr, c + dc)
                    if not (0 <= nr < row and 0 <= nc < col):
                        continue
                    if S[nr][nc] == '#':
                        continue
                    if dist[nr][nc] != -1:
                        continue
                    q.append((nr, nc))
                    dist[nr][nc] = dist[r][c] + 1
                    ans = max(ans, dist[nr][nc])
    print(ans)


def __starting_point():
    main()


__starting_point()
