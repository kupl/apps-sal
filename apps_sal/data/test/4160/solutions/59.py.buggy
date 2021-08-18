import math
from collections import Counter
from itertools import product


def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


x = ii()

cnt = 0
money = 100
while 1:
    if money >= x:
        print(cnt)
        return
    else:
        money += money // 100
        cnt += 1
