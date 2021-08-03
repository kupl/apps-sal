import time
import io
import math
import random


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Time : %f" % (time.time() - t))
        return res

    return tmp


n = int(input())
array = []
for i in range(n):
    str = input().split(' ')
    array.append([int(str[0]), int(str[1])])

summ = 0
x = array[0][0]
y = array[0][1]
for i in range(x * 100, y * 100):
    coord = i / 100
    f = True
    for j in range(1, len(array)):
        if array[j][0] <= coord <= array[j][1]:
            f = False
    if f:
        # print(coord)
        summ = summ + 1

print(int(round(summ / 100)))
