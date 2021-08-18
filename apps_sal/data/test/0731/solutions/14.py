import sys

w, m, k = (int(x) for x in sys.stdin.readline().split(' '))
n = w // k


def S(x):
    i = 0
    while x:
        i += 1
        x //= 10
    return i


c = 0
l = S(m)
while True:
    num = 10 ** l - m
    if n > num * l:
        n -= num * l
        c += num
        m = 10 ** l
        l += 1
    else:
        c += n // l
        break
print(c)
