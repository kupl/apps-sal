import sys
import os
import io
input = sys.stdin.readline
# input_all = sys.stdin.read
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# input_all = io.BytesIO(os.read(0,os.fstat(0).st_size)).read


def read_int():
    return map(int, input().split())


def read_list():
    return list(map(int, input().split()))


def print_list(l):
    print(' '.join(map(str, l)))
# import heapq as hq
# import bisect as bs
# from collections import deque as dq
# from collections import defaultdict as dc
# import math

# f = open('test.py')
# input = f.readline
# input_all = f.read


N = int(input())
for _ in range(N):
    n, k, l = read_list()
    d = read_list()
    if max(d) > l:
        print('No')
    else:

        # print(dic)
        flag = True
        tt = 2 * k
        now = tt
        for i in range(n):
            if d[i] + k <= l:
                tmp = tt
            else:
                tm = d[i] + k - l
                tmp = [tm, 2 * k - tm]
            # print(tmp)
            # tmp = dic[d[i]]
            if tmp == tt:
                now = tt
            elif now == tt:
                now = tmp
            else:
                now = [max(now[0] + 1, tmp[0]), min(now[1] + 1, tmp[1])]
                if now[0] > now[1]:
                    flag = False
                    break
        if flag:
            print('Yes')
        else:
            print('No')
