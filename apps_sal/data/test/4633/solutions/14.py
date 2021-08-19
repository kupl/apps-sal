"""
Author: AsilenceBTF
Blog: asilencebtf.top
Date: 2020-05-28 13:02:12
LastEditTime: 2020-09-04 23:11:19
"""


def f(n):
    res = 0
    while n > 0:
        res = res + 1
        n = n // 10
    return res


def check(n):
    res = 0
    while n > 0:
        res = res + n % 10
        n = n // 10
    return res


for _ in range(int(input())):
    (n, s) = list(map(int, input().split()))
    len = f(n)
    ans = pow(10, 20)
    if check(n) <= s:
        ans = 0
    for i in range(0, len):
        p = n // pow(10, i + 1)
        p = p * pow(10, i + 1)
        p = p + pow(10, i + 1)
        if check(p) <= s:
            if ans > p - n:
                ans = p - n
    print(ans)
