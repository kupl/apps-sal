from itertools import *


def r():
    return list(map(int, input().split()))


(w, l) = r()
v = [0, *accumulate(r())]
print(min((v[i] - v[i - l] for i in range(l, w))))
