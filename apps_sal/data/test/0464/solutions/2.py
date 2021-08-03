r, c = map(int, input().split())
board = [input() for i in range(r)]
stars = sum([i.count('*') for i in board])


def valid(x, y):
    nonlocal r, c
    return 0 <= x < r and 0 <= y < c


def f(r, c):
    nonlocal board
    cnt = 1

    for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
        i = 1
        while valid(r + i * dr, c + i * dc):
            if board[r + i * dr][c + i * dc] == '*':
                cnt += 1
            else:
                break
            i += 1

    return cnt


for i in range(1, r - 1):
    for j in range(1, c - 1):
        if '*' == board[i][j] == board[i - 1][j] == board[i + 1][j] == board[i][j - 1] == board[i][j + 1]:
            if f(i, j) == stars:
                print("YES")
                return

print("NO")
