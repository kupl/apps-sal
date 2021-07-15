positions = [[0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1], [0, 2, 1]]
n = int(input())
x = int(input())
k = n % 6
print(positions[k][x])
