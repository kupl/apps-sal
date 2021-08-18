h, w, k = map(int, input().split())
board = [[-1 for j in range(w)] for i in range(h)]
for i in range(h):
    color = input()
    for j in range(w):
        if color[j] == "
        board[i][j] = 1
        else:
            board[i][j] = 0
ans = 0

for row_choose in range(1 << h):
    for col_choose in range(1 << w):
        count = 0
        for i in range(h):
            for j in range(w):
                if not (row_choose & (1 << i)) and not (col_choose & (1 << j)) and board[i][j]:
                    count += 1
        if count == k:
            ans += 1

print(ans)
