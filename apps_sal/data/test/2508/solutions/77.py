import collections

H, W, K = [int(x) for x in input().split()]
X1, Y1, X2, Y2 = [int(x) for x in input().split()]
C = [input().strip() for _ in range(H)]

ans = [[float("inf")] * W for j in range(H)]

q = collections.deque()
q.append((X1 - 1, Y1 - 1))

ans[X1 - 1][Y1 - 1] = 0

while q:
    cx, cy = q.popleft()
    cc = ans[cx][cy]
    nc = cc + 1

    for i in range(1, K + 1):
        if cy + i >= W or C[cx][cy + i] == "@":
            break
        if ans[cx][cy + i] <= nc - 1:
            break
        if ans[cx][cy + i] <= nc:
            continue
        ans[cx][cy + i] = nc
        q.append((cx, cy + i))
    for i in range(1, K + 1):
        if cy - i <= -1 or C[cx][cy - i] == "@":
            break
        if ans[cx][cy - i] <= nc - 1:
            break
        if ans[cx][cy - i] <= nc:
            continue
        ans[cx][cy - i] = nc
        q.append((cx, cy - i))
    for i in range(1, K + 1):
        if cx - i <= -1 or C[cx - i][cy] == "@":
            break
        if ans[cx - i][cy] <= nc - 1:
            break
        if ans[cx - i][cy] <= nc:
            continue
        ans[cx - i][cy] = nc
        q.append((cx - i, cy))
    for i in range(1, K + 1):
        if cx + i >= H or C[cx + i][cy] == "@":
            break
        if ans[cx + i][cy] <= nc - 1:
            break
        if ans[cx + i][cy] <= nc:
            continue
        ans[cx + i][cy] = nc
        q.append((cx + i, cy))

if ans[X2 - 1][Y2 - 1] == float("inf"):
    print((-1))
else:
    print((ans[X2 - 1][Y2 - 1]))
