n, x = int(input()), int(input())
n %= 6
ans = [[0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1], [0, 2, 1]]
print(ans[n][x])
