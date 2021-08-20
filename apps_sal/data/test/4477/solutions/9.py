import sys
import math
import io
import os


def data():
    return sys.stdin.readline().strip()


def mdata():
    return list(map(int, data().split()))


def outl(var):
    sys.stdout.write(' '.join(map(str, var)) + '\n')


def out(var):
    sys.stdout.write(str(var) + '\n')


mod = int(1000000000.0) + 7
for t in range(int(data())):
    s = data()
    ans = 10 * int(s[0]) - 10 + len(s) * (len(s) + 1) // 2
    out(ans)
