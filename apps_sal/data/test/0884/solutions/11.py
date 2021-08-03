import sys
import time

mod = 998244353


def calc(a, b):
    if(a < b):
        a, b = b, a
    s = 0
    t = 1
    for i in range(b + 1):
        s = s + t
        t = t * (a - i) // (i + 1) * (b - i)
    return s


(a, b, c) = list(map(int, sys.stdin.readline().split()))
start = time.time()
print(((calc(a, b) * calc(b, c) * calc(c, a)) % mod))
end = time.time()
# print(end-start);
