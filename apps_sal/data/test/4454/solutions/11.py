"""
NTC here
"""
from sys import setcheckinterval, stdin, setrecursionlimit
setcheckinterval(1000)
setrecursionlimit(10 ** 7)


def iin():
    return int(stdin.readline())


def lin():
    return list(map(int, stdin.readline().split()))


for _ in range(iin()):
    n = iin()
    a = lin()
    sm = sum(a)
    print((sm + n - 1) // n)
