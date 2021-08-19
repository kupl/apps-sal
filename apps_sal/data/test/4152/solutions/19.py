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


def find_lt(a, x):  # 'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):  # 'Find leftmost value greater than x'
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
# ---------------------Template ends-------------sdpt,sdpt131[Sudipta Banik]---------------------


n = nexint()
a = readlist()
a.sort()
mp = {}
for el in a:
    if el in mp:
        mp[el] += 1
    else:
        mp[el] = 1
# b = [False]*n
ans = 0
for i in range(n):
    k = 0
    flg = False
    while (k <= 30):
        key = (1 << k) - a[i]
        if key in mp:
            if (1 << k) != 2 * a[i]:
                flg = True
                break
            else:
                if(mp[a[i]] > 1):
                    flg = True
                    break
        k += 1

    if not flg:
        ans += 1

cout(ans)


# val , m = readline()
# coin = readlist()

# cache = []
# for i in range(m):
#     cache.append([-1 for _ in range(val+1)])

# def DP(i,left):

#     if left < 0:
#         return  0
#     if i == m:
#         return (1 if left == 0 else 0)
#     if cache[i][left] >= 0:
#         return cache[i][left]

#     if left == 0:
#         return  1

#     x = DP(i+1,left)
#     if(left>=coin[i]):
#         x+=DP(i,left-coin[i])
#     cache[i][left] =x
#     return x

# def DP_iter(val):
#     dp = []
#     for i in range(m):
#         dp.append([0 for _ in range(val+1)])
#     for X in range(val+1):
#         for i in range(m-2,0,-1):
#             if X < coin[i]:
#                 dp[i][X] = 0
#             if X == coin[i]:
#                 dp[i][X] = 1
#             else:
#                 dp[i][X] = (dp[i+1][X]+dp[i][X-coin[i]])
#     for i in range(m):
#         printr(dp[i])


#     return dp[m-1][X]


# cout(DP(0,val))
# cout(DP_iter(val))
