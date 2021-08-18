import itertools
import math
import random

import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time() - t))
        return res

    return tmp


def genArray(length, lower, upper):
    return [random.randint(lower, upper) for i in range(length)]

#print(genArray(5, 4, 9))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n, k = map(int, input().split(' '))
k = n - k

if k == 0:
    print(-1)
    return
else:
    array = [0 for i in range(n)]
    for j in range(k):
        array[j] = (j - 1) % (k) + 1
    for j in range(k, n):
        array[j] = j + 1


ar = [i + 1 for i in range(n)]
# print(ar)
# print(array)

total = 0
for i in range(n):
    if gcd(ar[i], array[i]) == 1:
        total += 1

# print(total)

str = array.__str__().replace('[', '').replace(']', '').replace(',', '')
print(str)
