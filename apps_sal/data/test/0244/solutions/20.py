n = int(input())
k = int(input())
n %= 6
d = [[0, 1, 1, 2, 2, 0], [1, 0, 2, 1, 0, 2], [2, 2, 0, 0, 1, 1]]
print(d[k][n])

