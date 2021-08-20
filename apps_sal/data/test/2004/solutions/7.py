import math
n = int(input())
m = n + math.floor(n / 2)
print(m)
for i in range(2, n + 1, 2):
    print(i, end=' ')
for i in range(1, n + 1, 2):
    print(i, end=' ')
for i in range(2, n + 1, 2):
    print(i, end=' ')
