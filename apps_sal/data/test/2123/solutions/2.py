import itertools
import math
import random

import time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp

def genArray(length, lower, upper):
    return [random.randint(lower, upper) for i in range(length)]


n = int(input())
array = list(map(int, input().split(' ')))

print(max(array))
