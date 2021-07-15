n,m = list(map(int,input().split()))
mat = [list(map(int,input().split())) for _ in range(n)]

# xr = 0
# for l in mat:
#     for i in l:
#         xr ^= i
#
# if xr == 0:
#     print('NIE')
#     return

res = []

for i in range(n):
    prev = -1
    for j in range(m):
        if prev == -1:
            prev = mat[i][j]
        elif prev != mat[i][j]:
            # mat[i][j - 1] と mat[i][j]
            xr = 0
            for k in range(n):
                if k != i:
                    xr ^= mat[k][0]
            if xr ^ mat[i][j - 1] != 0:
                res = [1] * (i) + [j] + [1] * (n - i - 1)
            else:
                res = [1] * (i) + [j + 1] + [1] * (n - i - 1)
            print('TAK')#, mat[i][j - 1], mat[i][j], xr)
            print(*res)
            return

xr = 0
for i in range(n):
    xr ^= mat[i][0]

if xr == 0:
    print('NIE')
else:
    print('TAK')
    res = [1] * n
    print(*res)

