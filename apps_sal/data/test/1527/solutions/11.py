from collections import deque
import copy

H, W = map(int, input().split())
S = [[x for x in input()] for _ in range(H)]
start_list = []
length = [[-1] * W for _ in range(H)]
ans = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            start_list.append((i, j))

for start in start_list:
    h, w = start
    d = deque([(h, w)])
    T = copy.deepcopy(S)
    L = copy.deepcopy(length)
    L[h][w] = 0
    T[h][w] = '
    while d:
        h, w = d.popleft()

        if h - 1 >= 0 and T[h - 1][w] == '.':
            d.append((h - 1, w))
            L[h - 1][w] = L[h][w] + 1
            T[h - 1][w] = '
            ans = max(ans, L[h - 1][w])

        if h + 1 <= H - 1 and T[h + 1][w] == '.':
            d.append((h + 1, w))
            L[h + 1][w] = L[h][w] + 1
            T[h + 1][w] = '
            ans = max(ans, L[h + 1][w])

        if w - 1 >= 0 and T[h][w - 1] == '.':
            d.append((h, w - 1))
            L[h][w - 1] = L[h][w] + 1
            T[h][w - 1] = '
            ans = max(ans, L[h][w - 1])

        if w + 1 <= W - 1 and T[h][w + 1] == '.':
            d.append((h, w + 1))
            L[h][w + 1] = L[h][w] + 1
            T[h][w + 1] = '
            ans = max(ans, L[h][w + 1])

print(ans)
