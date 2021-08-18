from math import floor
from math import sqrt


def f(bb, nn):
    if(nn < bb):
        return nn
    else:
        return f(bb, floor(nn / bb)) + (nn % bb)


n = int(input())
s = int(input())

if n == s:
    print((n + 1))
    return
elif n < s:
    print((-1))
    return

for i in range(2, int(sqrt(n)) + 2):
    if s == f(i, n):
        print(i)
        return

for i in reversed(list(range(1, int(sqrt(n)) + 2))):
    if (n - s) % i == 0:
        tmpb = (n - s) // i + 1
        if tmpb >= sqrt(n) and f(tmpb, n) == s:
            print(tmpb)
            return
print((-1))
