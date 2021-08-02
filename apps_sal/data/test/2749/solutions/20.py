h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
mat = [[0] * w for i in range(h)]
idx = 0
for y in range(h):
    for x in range(w):
        if y % 2 == 0:
            mat[y][x] = idx + 1
        else:
            mat[y][w - 1 - x] = idx + 1
        a[idx] -= 1
        if a[idx] == 0:
            idx += 1

for y in range(h):
    print((" ".join(list(map(str, mat[y])))))
