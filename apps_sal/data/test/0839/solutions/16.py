from sys import stdin as cin
from itertools import permutations as p
a = [] * 5
for i in range(5):
    a.append(list(map(int, cin.readline().split())))
b = list(p([0, 1, 2, 3, 4]))
sum = 0
max = 0
for x in b:
    sum = a[x[0]][x[1]] + a[x[2]][x[3]] + a[x[1]][x[2]] + a[x[3]][x[4]] + a[x[2]][x[3]] + a[x[3]][x[4]] + a[x[1]][x[0]] + a[x[3]][x[2]] + a[x[2]][x[1]] + a[x[4]][x[3]] + a[x[3]][x[2]] + a[x[4]][x[3]]
    if sum > max:
        max = sum
print(max)
