n = int(input())
x = int(input())
res = [[0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1], [0, 2, 1]]
pos = n % 6
print(res[pos][x])
