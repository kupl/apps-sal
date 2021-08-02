from collections import deque
h, w = list(map(int, input().split()))
num = [list(input()) for _ in range(h)]
seen = [[False] * w for _ in range(h)]
queue = deque()
queue.append([0, 0])
ans = [[0] * w for _ in range(h)]
seen[0][0] = True
for i in range(h * w * 100):
    if len(queue) == 0:
        break
    cnt = queue.popleft()
    if num[max(0, cnt[0] - 1)][cnt[1]] == "." and seen[max(0, cnt[0] - 1)][cnt[1]] == False:
        queue.append([cnt[0] - 1, cnt[1]])
        seen[max(0, cnt[0] - 1)][cnt[1]] = True
        ans[max(0, cnt[0] - 1)][cnt[1]] = ans[cnt[0]][cnt[1]] + 1
    if num[min(h - 1, cnt[0] + 1)][cnt[1]] == "." and seen[min(h - 1, cnt[0] + 1)][cnt[1]] == False:
        queue.append([cnt[0] + 1, cnt[1]])
        seen[min(h - 1, cnt[0] + 1)][cnt[1]] = True
        ans[min(h - 1, cnt[0] + 1)][cnt[1]] = ans[cnt[0]][cnt[1]] + 1
    if num[cnt[0]][max(cnt[1] - 1, 0)] == "." and seen[cnt[0]][max(cnt[1] - 1, 0)] == False:
        queue.append([cnt[0], cnt[1] - 1])
        seen[cnt[0]][max(cnt[1] - 1, 0)] = True
        ans[cnt[0]][max(cnt[1] - 1, 0)] = ans[cnt[0]][cnt[1]] + 1
    if num[cnt[0]][min(w - 1, cnt[1] + 1)] == "." and seen[cnt[0]][min(w - 1, cnt[1] + 1)] == False:
        queue.append([cnt[0], cnt[1] + 1])
        seen[cnt[0]][min(w - 1, cnt[1] + 1)] = True
        ans[cnt[0]][min(w - 1, cnt[1] + 1)] = ans[cnt[0]][cnt[1]] + 1
if seen[-1][-1] == False:
    print((-1))
else:
    cnt3 = 0
    for i in range(h):
        cnt3 += num[i].count(".")
    print((cnt3 - ans[-1][-1] - 1))
