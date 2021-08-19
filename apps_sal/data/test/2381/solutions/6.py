import datetime
import string
import re
import math


def isort(list, _beg, _end):
    if _beg < _end:
        beg = _beg
        end = _end
        pivot = abs(list[int((beg + end) / 2)])
        while True:
            while abs(list[beg]) < pivot:
                beg += 1
            while abs(list[end]) > pivot:
                end -= 1
            if beg <= end:
                tmp = list[beg]
                list[beg] = list[end]
                list[end] = tmp
                beg += 1
                end -= 1
            else:
                break
        isort(list, _beg, end)
        isort(list, beg, _end)


def searchByBool(list):
    for i in range(len(list)):
        if check(list[i]):
            return i
    return -1


def check(num):
    if num >= 0:
        return True
    else:
        return False


sp = list(map(int, input().split()))
N = sp[0]
K = sp[1]
alist = list(map(int, input().split()))
klist = []
isK = True
isort(alist, 0, len(alist) - 1)
alist.reverse()
numMinus = 0
for i in range(K):
    if check(alist[i]) == False:
        numMinus += 1
if numMinus % 2 == 0:
    isK = False
if isK and K < N:
    _right = -1
    _left = -1
    for right in range(K, N):
        if check(alist[K - 1]) != check(alist[right]):
            _right = right
            break
    for left in range(K):
        if check(alist[K - 1 - left]) != check(alist[K]):
            _left = left
            break
    isK = False
    if _right != -1 and _left != -1:
        if abs(alist[K - 1 - left] * alist[_right]) < abs(alist[K - 1] * alist[K]):
            alist[K - 1 - _left] = alist[K]
        else:
            alist[K - 1] = alist[_right]
    elif _right == -1 and _left != -1:
        alist[K - 1 - _left] = alist[K]
    elif _right != -1 and _left == -1:
        alist[K - 1] = alist[_right]
    else:
        isK = True
if isK:
    alist.reverse()
klist = alist[0:K]
multi = klist[0]
for i in range(1, K):
    multi *= klist[i]
    multi = multi % 1000000007
print(multi)
