# import sys
# sys.setrecursionlimit(10 ** 9)

# H, W = map(int, input().split())
# L = []
# for _ in range(H):
#     s = input()
#     a = []
#     for i in range(len(s)):
#         a.append(s[i])
#     L.append(a)

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]


# def dfs(h, w, dp, ans, count):
#     if L[h][w] == '#':
#         return ans
#     elif (L[h][w] == '.' and dp[h][w] == -1):
#         dp[h][w] = 0

#     for i in range(4):
#         if w + dx[i] >= 0 and w + dx[i] < W and h + \
#                 dy[i] >= 0 and h + dy[i] < H:
#             if L[h + dy[i]][w + dx[i]] == '.' and dp[h + dy[i]][w + dx[i]] == -1:
#                 count += 1
#                 ans[h + dy[i]][w + dx[i]
#                                ] = min(ans[h + dy[i]][w + dx[i]], count)
#                 return dfs(h + dy[i], w + dx[i], dp, ans, count)
#             elif L[h + dy[i]][w + dx[i]] == '#':
#                 continue

#     return ans


# max_count = 0
# ans = [[100000000] * W for _ in range(H)]
# for i in range(H):
#     for j in range(W):
#         dp = [[-1] * W for _ in range(H)]
#         count = dfs(i, j, dp, ans, 0)
#         print(count)
#         # max_count = max(max_count, count)

# print(max_count)

# 幅優先探索
from collections import deque
H, W = list(map(int, input().split()))
L = []
for _ in range(H):
    s = input()
    a = []
    for i in range(len(s)):
        a.append(s[i])
    L.append(a)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    dp = [[10000000] * W for _ in range(H)]
    dp[y][x] = 0
    if L[y][x] == '#':
        return dp
    else:
        d = deque()
        d.append([x, y])
        while len(d) > 0:
            s = d.popleft()
            for i in range(4):
                if (s[1] +
                    dy[i] >= 0 and s[1] +
                    dy[i] < H and s[0] +
                    dx[i] >= 0 and s[0] +
                        dx[i] < W):
                    if L[s[1] +
                         dy[i]][s[0] +
                                dx[i]] == '.' and dp[s[1] +
                                                     dy[i]][s[0] +
                                                            dx[i]] == 10000000:
                        d.append([s[0] + dx[i], s[1] + dy[i]])
                        dp[s[1] + dy[i]][s[0] + dx[i]] = dp[s[1]][s[0]] + 1

        return dp


max_num = 0
for i in range(H):
    for j in range(W):
        dp = bfs(j, i)
        for k in dp:
            for p in k:
                if (p == 10000000):
                    continue
                max_num = max(max_num, p)
print(max_num)

