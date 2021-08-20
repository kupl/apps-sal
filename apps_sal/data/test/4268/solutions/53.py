import math
(n, d) = (int(i) for i in input().split())
list_x = [[int(i) for i in input().split()] for j in range(0, n)]
count = 0
tmp = 0
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(0, d):
            tmp += pow(list_x[i][k] - list_x[j][k], 2)
        tmp = math.sqrt(tmp)
        if tmp.is_integer():
            count += 1
        tmp = 0
print(count)
