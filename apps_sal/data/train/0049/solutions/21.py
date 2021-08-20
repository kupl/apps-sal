import bisect as b
from collections import OrderedDict
num = []


def Classy(pos, count, current):
    if pos == 18:
        num.append(current)
        return
    Classy(pos + 1, count, current * 10)
    if count < 3:
        for i in range(1, 10):
            Classy(pos + 1, count + 1, current * 10 + i)


Classy(0, 0, 0)
num = list(OrderedDict.fromkeys(num))
num.pop(0)
num.insert(len(num) + 1, 1000000000000000000)
T = int(input())
while 0 < T:
    (L, R) = [int(x) for x in input().split(' ')]
    ans = b.bisect_right(num, R, lo=0, hi=len(num)) - b.bisect_left(num, L, lo=0, hi=len(num))
    print(int(ans))
    T = T - 1
