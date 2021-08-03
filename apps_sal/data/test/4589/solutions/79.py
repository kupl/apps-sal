# 0: 下、1: 右、2: 上、3: 左、4: 右下、5: 右上、6: 左上、7: 左下
dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

# 入力
H, W = map(int, input().split())
S = [input() for _ in range(H)]

# Python3 では str 型の要素の書き換えはできない
# 答えを格納する二次元配列を別途用意する ('.' のところは 0 とする)
result = [[0 if v == '.' else '#' for v in row] for row in S]

# 各マス (i, j) について順に処理
for i in range(H):
    for j in range(W):
        if S[i][j] != '.':
            continue
        for d in range(8):
            ni = i + dx[d]
            nj = j + dy[d]
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if S[ni][nj] == '#':
                result[i][j] += 1

for row in result:
    # 出力形式に合わせて出力
    print(*row, sep='')
