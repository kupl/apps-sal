h, w = map(int, input().split())
lis = [list(input()) for i in range(h)]

ans = [[0] * w for i in range(h)]

for i in range(h):
    for j in range(w):
        x, y = 0, 0
        if lis[i][j] == "#":
            ans[i][j] = 1
            for a in range(-1, 2):
                if 0 <= i + a < h and lis[i + a][j] == "#" and a != 0:
                    x += 1
            ans[i][j] += x
            for b in range(-1, 2):
                if 0 <= j + b < w and lis[i][j + b] == "#" and b != 0:
                    y += 1
            ans[i][j] += y
            if ans[i][j] == 1:
                print("No")
                return
        else:
            ans[i][j] = 0

print("Yes")
