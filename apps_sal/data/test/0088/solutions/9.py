from math import *


def bindec(ch):
    r = 0
    p = 1
    n = len(ch)
    for k in range(n):
        r += int(ch[n - 1 - k]) * p
        p *= 2
    return r


(a, b) = list(map(int, input().split()))
la = int(log(a, 2)) + 1
lb = int(log(b, 2)) + 1
r = 0
ch = ''
for k in range(la, lb + 1):
    for i in range(1, k):
        ch = '1' * i + '0' + '1' * (k - i - 1)
        if bindec(ch) > b:
            break
        elif bindec(ch) >= a:
            r += 1
print(r)
