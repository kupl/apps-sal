import sys
import math
mod = 10 ** 9 + 7
md = 998244353


def input():
    return sys.stdin.readline().strip()


def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    (a, b) = inp()
    s = str(input())
    ans = []
    c = 0
    for i in s:
        if i == '1':
            c += 1
        else:
            if c == 0:
                continue
            ans.append(c)
            c = 0
    if c > 0:
        ans.append(c)
    flag = False
    c = 0
    res = []
    for i in s:
        if i == '1':
            flag = True
        if flag == True:
            if i == '0':
                c += 1
            else:
                if c == 0:
                    continue
                res.append(c)
                c = 0
    fin = 0
    if len(ans) > 0:
        fin += a
    if len(ans) > 1:
        for i in range(len(res)):
            if res[i] * b > a:
                fin += a
            else:
                fin += res[i] * b
    print(fin)
