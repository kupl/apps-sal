import math
n = int(input())
c = 0
num = 0
while c < n:
    num += 5
    tnum = num
    while tnum % 5 == 0:
        tnum //= 5
        c += 1
if c > n:
    print(0)
else:
    print(5)
    for i in range(5):
        print(num + i, end=' ')
