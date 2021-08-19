import sys
import math
import heapq
import random
import collections
import datetime


def main():
    t1 = list(map(int, input().strip().split(':')))
    t2 = list(map(int, input().strip().split(':')))
    t1_ = datetime.timedelta(hours=t1[0], minutes=t1[1])
    t2_ = datetime.timedelta(hours=t2[0], minutes=t2[1])
    t3_ = t1_ - t2_
    s = str(t3_)
    if len(s[-8:-3]) == 4:
        print('0' + s[-8:-3])
    elif len(s[-8:-3]) == 5 and s[-8] == ' ':
        print('0' + s[-7:-3])
    else:
        print(s[-8:-3])


def __starting_point():
    main()


__starting_point()
