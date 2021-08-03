from collections import deque
h, w = list(map(int, input().split()))
queue = deque()
s = [list(input()) for _ in range(h)]
seen = [[False] * w for _ in range(h)]
queue.append([0, 0])
ans = [[1000000000] * w for _ in range(h)]
seen[0][0] = True
ans[0][0] = 1
for i in range(h * w * 10):
    if len(queue) == 0:
        break
    cnt = queue.popleft()
    if cnt[0] != 0:
        if seen[cnt[0] - 1][cnt[1]] == False and s[cnt[0] - 1][cnt[1]] == ".":
            queue.append([cnt[0] - 1, cnt[1]])
            ans[cnt[0] - 1][cnt[1]] = ans[cnt[0]][cnt[1]] + 1
            seen[cnt[0] - 1][cnt[1]] = True
    if cnt[1] != 0:
        if seen[cnt[0]][cnt[1] - 1] == False and s[cnt[0]][cnt[1] - 1] == ".":
            queue.append([cnt[0], cnt[1] - 1])
            ans[cnt[0]][cnt[1] - 1] = ans[cnt[0]][cnt[1]] + 1
            seen[cnt[0]][cnt[1] - 1] = True
    if cnt[0] != h - 1:
        if seen[cnt[0] + 1][cnt[1]] == False and s[cnt[0] + 1][cnt[1]] == ".":
            queue.append([cnt[0] + 1, cnt[1]])
            ans[cnt[0] + 1][cnt[1]] = ans[cnt[0]][cnt[1]] + 1
            seen[cnt[0] + 1][cnt[1]] = True
    if cnt[1] != w - 1:
        if seen[cnt[0]][cnt[1] + 1] == False and s[cnt[0]][cnt[1] + 1] == ".":
            queue.append([cnt[0], cnt[1] + 1])
            ans[cnt[0]][cnt[1] + 1] = ans[cnt[0]][cnt[1]] + 1
            seen[cnt[0]][cnt[1] + 1] = True
cnt2 = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            cnt2 += 1
if seen[-1][-1] == False:
    print((-1))
else:
    print((cnt2 - ans[-1][-1]))
