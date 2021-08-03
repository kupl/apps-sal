from math import ceil

M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

temp = input().split()
m = int(temp[0])
d = int(temp[1])
t = M[m - 1] + d - 1
print(ceil(t / 7))
