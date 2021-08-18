h, w = map(int, input().split())

sl = [list(input()) for _ in range(h)]
ans = [[0] * (w + 2) for _ in range(h + 2)]

for i in range(h):
    for j in range(w):
        row = i + 1
        col = j + 1
        if sl[i][j] == '
          ans[row][col] = '
           if ans[row - 1][col] != '
              ans[row - 1][col] += 1
            if ans[row + 1][col] != '
              ans[row + 1][col] += 1
            if ans[row][col - 1] != '
              ans[row][col - 1] += 1
            if ans[row][col + 1] != '
              ans[row][col + 1] += 1
            if ans[row - 1][col - 1] != '
              ans[row - 1][col - 1] += 1
            if ans[row - 1][col + 1] != '
              ans[row - 1][col + 1] += 1
            if ans[row + 1][col - 1] != '
              ans[row + 1][col - 1] += 1
            if ans[row + 1][col + 1] != '
              ans[row + 1][col + 1] += 1


for i in range(h + 2):
    if i != 0 and i != h + 1:
        print(*ans[i][1:-1], sep='')
