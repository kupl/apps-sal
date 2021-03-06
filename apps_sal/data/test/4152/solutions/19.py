from sys import stdin, stdout
from bisect import bisect_left, bisect_right
from collections import defaultdict
import math
cin = stdin.readline


def cout(x):
    stdout.write(str(x) + '\n')


def nexint():
    return int(stdin.readline())


def readline():
    return list(map(int, stdin.readline().split()))


def readlist():
    return list(map(int, stdin.readline().split()))


def sorted_indexes(arr):
    return sorted(list(range(len(arr))), key=arr.__getitem__)


def printr(arr):
    [stdout.write(str(x) + ' ') for x in arr]
    cout('')


def find_lt(a, x):
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def binarySearch(arr, l, r, x):
    lo = l
    hi = r
    while hi >= lo:
        mid = (hi + lo) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


n = nexint()
a = readlist()
a.sort()
mp = {}
for el in a:
    if el in mp:
        mp[el] += 1
    else:
        mp[el] = 1
ans = 0
for i in range(n):
    k = 0
    flg = False
    while k <= 30:
        key = (1 << k) - a[i]
        if key in mp:
            if 1 << k != 2 * a[i]:
                flg = True
                break
            elif mp[a[i]] > 1:
                flg = True
                break
        k += 1
    if not flg:
        ans += 1
cout(ans)
