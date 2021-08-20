import math


def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n // b) + n % b


def build_div(x):
    i = 1
    ret = []
    if x < 0:
        return ret
    while True:
        if i * i > x:
            break
        if x % i == 0:
            ret.append(i)
            ret.append(x // i)
        i += 1
    return sorted(ret)


n = int(input())
s = int(input())
b = -1
if n == s:
    print(n + 1)
else:
    for i in range(2, math.ceil(math.sqrt(n))):
        if f(i, n) == s:
            b = i
            print(b)
            break
    if b == -1:
        div = build_div(n - s)
        for i in div:
            if f(i + 1, n) == s:
                b = i + 1
                print(b)
                break
    if b == -1:
        print(-1)
