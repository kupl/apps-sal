from collections import deque
H,W = map(int,input().split())
n = int(input())
a_ls = list(map(int, input().split()))
color_q = deque()
for color, times in enumerate(a_ls,1):
    for _ in range(times):
        color_q.append(color)
ans_mat = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        ans_mat[y][x] = color_q.popleft()
for i,y in enumerate(range(H)):
    ans_ls = ans_mat[y]
    if i % 2 == 1:
        ans_ls = ans_ls[::-1]
    ans_ls = list(map(str,ans_ls))
    print(' '.join(ans_ls))
