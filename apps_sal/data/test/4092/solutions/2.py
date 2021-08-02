# Created by: WeirdBugsButOkay
# 28-09-2020, 13:52:29

import math


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dict = {}
    dict[0] = 1
    sum, ans = 0, 0
    for i in range(0, n):
        sum += a[i]
        #print(i, sum)
        if sum in list(dict.keys()):
            ans += 1
            dict = {}
            dict[0] = 1
            sum = a[i]
            dict[sum] = 1
            # print("haha")
        else:
            dict[sum] = 1
    print(ans)


t = 1
#t = int(input())
for _ in range(0, t):
    solve()
