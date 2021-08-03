import sys
n = int(input())
m = int(input())
z = [[0, 1, 2],
     [1, 0, 2],
     [1, 2, 0],
     [2, 1, 0],
     [2, 0, 1],
     [0, 2, 1]]
print(z[n % 6][m])
