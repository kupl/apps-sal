import sys

input = sys.stdin.readline
H, W = map(int, input().split())
S = [(input()) for _ in range(H)]
T = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
    for w in range(W):
        for i in range(h - 1, h + 2):
            for j in range(w - 1, w + 2):
                if i < 0 or j < 0 or i >= H or j >= W:
                    continue
                else:
                    if S[h][w] == '
                        T[h][w] = -1
                    elif S[i][j] == '
                        T[h][w] += 1

for t in T:
    print((''.join(map(str, t))).replace('-1', '
