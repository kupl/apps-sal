from collections import deque


def LI():
    return list(map(int, input().split()))


def LSH(h):
    return [input() for _ in range(h)]


(H, W) = LI()
Fi = LSH(H)
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
for sh in range(H):
    for sw in range(W):
        if Fi[sh][sw] == '#':
            continue
        d = deque()
        d.append([sh, sw])
        looked = [[0 for i in range(W)] for j in range(H)]
        looked[sh][sw] = 1
        while d:
            (h, w) = d.popleft()
            for i in move:
                a = h + i[0]
                b = w + i[1]
                if not 0 <= a < H or not 0 <= b < W or Fi[a][b] == '#' or (looked[a][b] != 0):
                    continue
                d.append([a, b])
                looked[a][b] = looked[h][w] + 1
            if len(d) == 0:
                ans = max(ans, looked[h][w] - 1)
print(ans)
