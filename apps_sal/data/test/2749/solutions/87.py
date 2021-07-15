h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

mat = [[0] * w for _ in range(h)]

i = 0
j = 0
num = 1
while True:
    mat[j][i] = num
    a[num-1] -= 1
    if a[num-1] == 0:
        num += 1
    if i <= w-2:
        i += 1
    elif i == w-1:
        if j == h-1:
            break
        i = 0
        j += 1

for i in range(h):
    if i % 2 == 1:
        tmp = mat[i]
        tmp.reverse()
        mat[i] = tmp

for i in range(h):
    for j in range(w-1):
        print(mat[i][j], end = ' ')
    print(mat[i][-1])
