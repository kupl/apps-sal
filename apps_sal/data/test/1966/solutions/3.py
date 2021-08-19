n = int(input())
board = [[list(map(int, list(input()))) for i in range(n)]]
for _ in range(3):
    input()
    board.append([list(map(int, list(input()))) for i in range(n)])
var_ = ['1100', '1010', '1001', '0110', '0101', '0011']
ans = 4 * n ** 2
for pat in var_:
    now = 0
    for (ind, ch) in enumerate(list(map(int, list(pat)))):
        b = board[ind]
        for i in range(n):
            for j in range(n):
                if (i + j + ch) % 2 != b[i][j]:
                    now += 1
    ans = min(ans, now)
print(ans)
