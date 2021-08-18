n = int(input())
board = []
for i in range(n):
    r = input()
    board.append(r)
can = True
for i in range(n):
    row = board[i]
    for j in range(n):
        ele = row[j]
        c = 0
        ind_r = [j + 1, j - 1]
        ind_c = [i + 1, i - 1]
        for k in range(2):
            if ind_r[k] >= n or ind_r[k] < 0:
                continue

            else:
                if row[ind_r[k]] == 'o':
                    c += 1
        for k in range(2):
            if ind_c[k] >= n or ind_c[k] < 0:
                continue

            else:
                if board[ind_c[k]][j] == 'o':
                    c += 1
        if c % 2 != 0:
            can = False
            break
    if can == False:
        break
if can == True:
    print("YES")
else:
    print("NO")
