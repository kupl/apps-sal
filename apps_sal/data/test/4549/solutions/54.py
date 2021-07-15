h, w = list(map(int, input().split()))
table = [list(input()) for _ in range(h)]

mx = [0, 1, 0, -1]
my = [1, 0, -1, 0]
for i in range(h):
    for j in range(w):
        if table[i][j] == "#":
            for k in range(4):
                tx, ty = j + mx[k], i + my[k]
                if 0 <= tx < w and 0 <= ty < h and table[ty][tx] == "#":
                    break
            else:
                print("No")
                return
print("Yes")


