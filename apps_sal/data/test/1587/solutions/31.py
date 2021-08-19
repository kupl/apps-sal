import math
import collections
import itertools
import copy


def YesNo(Bool):
    if Bool:
        print('Yes')
    else:
        print('No')
    return


def resolve():
    N = int(input())
    C = input()
    l = 0
    r = N - 1
    lfound = False
    rfound = False
    cnt = 0
    while True:
        if C[l] == 'W':
            lfound = True
        else:
            l += 1
        if C[r] == 'R':
            rfound = True
        else:
            r -= 1
        if rfound and lfound:
            cnt += 1
            l += 1
            r -= 1
            rfound = False
            lfound = False
        if l >= r:
            break
    print(cnt)


resolve()
