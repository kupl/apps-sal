import sys
import copy
sys.setrecursionlimit(10000000)

h, w, k = list(map(int, input().split()))
ground = [list(input()) for j in range(h)]
ground2 = copy.deepcopy(ground)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def dfs(x, y, count):
    ground[y][x] = str(count)
    # print(y,x)
    for k in range(4):
        if 0 <= x + dx[k] < w and 0 <= y + dy[k] < h:
            if ground[y + dy[k]][x + dx[k]] == ".":
                dfs(x + dx[k], y + dy[k], count)


for j in range(h):
    for i in range(w):
        if ground[j][i] == ".":
            dfs(i, j, cnt)
            cnt += 1

arr = [[0, i] for i in range(cnt)]

for num in range(cnt):
    f = True
    for j in range(h):
        for i in range(w):
            # print(num,j,i,ground[j][i])
            if ground[j][i] == str(num):
                arr[num][0] += 1
                if i == 0 or i == w - 1 or j == 0 or j == h - 1:
                    f = False
                    arr[num][0] += 10**10
                    break
                    # print(num,j,i)
            if not f:
                break
        if not f:
            break

arr.sort()

for j in range(len(arr)):
    if arr[j][0] > 10**10:
        cnt -= 1

num_lake = cnt
ans = 0
"""
print(cnt,arr)
print(k)
"""
if cnt == k:
    print(ans)
    for j in range(h):
        print("".join(ground2[j][:]))
    return

for num in range(cnt):
    groundbef = ground[:][:]
    f = True
    cells = 0
    for j in range(h):
        for i in range(w):
            if ground[j][i] == str(arr[num][1]):
                if i < 0 or i > w - 1 or j < 0 or j > h - 1:
                    f = False
                    print("F", i, j)
                    break
                ground[j][i] = "*"
                cells += 1

    if not f:
        ground = groundbef[:][:]
        num_lake -= 1

    else:
        num_lake -= 1
        ans += cells

    if num_lake == k:
        break

for j in range(h):
    for i in range(w):
        if ground[j][i] == "*":
            continue
        else:
            ground[j][i] = "."

print(ans)
for j in range(h):
    print("".join(ground[j][:]))
