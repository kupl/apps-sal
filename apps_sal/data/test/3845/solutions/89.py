"""

Wは100で固定する。
1行目でできるかぎり連結成分の数が多くなるようにする。


W=100で固定し、白黒格子上になるように列を組む。
白と黒どちらかが規定数をオーバーしたら次の行で調整を入れて数を減らす。
ここでは、白が規定数に達したと仮定しよう。
白色の数に調整を入れたら、次の行では
"""
A, B = list(map(int, input().split()))
N = 100
n = N // 2
grid = [["#"] * N for _ in range(N)]
for i in range(n, N):
    for j in range(N):
        grid[i][j] = "."

A -= 1
B -= 1

for i in range(0, A // n * 2, 2):
    for j in range(0, N, 2):
        grid[i][j] = "."

for j in range(0, A % n * 2, 2):
    grid[A // n * 2][j] = "."

grid = grid[::-1]
for i in range(0, B // n * 2, 2):
    for j in range(0, N, 2):
        grid[i][j] = "#"

for j in range(0, B % n * 2, 2):
    grid[B // n * 2][j] = "#"

print((" ".join([str(N), str(N)])))
for i in range(N):
    print(("".join(grid[i])))
