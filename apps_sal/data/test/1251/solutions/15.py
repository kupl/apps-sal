import threading
from sys import setrecursionlimit
from sys import stdin
import sys
def g(): return stdin.readline().strip()
def gl(): return g().split()
def gil(): return [int(var) for var in gl()]
def gfl(): return [float(var) for var in gl()]
def gcl(): return list(g())
def gbs(): return [int(var) for var in g()]


mod = int(1e9) + 7
inf = float("inf")


def main():
    n, = gil()
    a = gil()

    def fun(a):
        ans = 0
        n = len(a)
        off = min(a)
        for i in range(n):
            a[i] -= off
        ans += off
        # print(a, off)
        buff = []
        while a:
            if a[-1]:
                buff.append(a.pop())
            else:
                a.pop()
                if buff:
                    ans += fun(buff)
                buff = []

        if buff:
            ans += fun(buff)

        return min(ans, n)

    print(fun(a))


setrecursionlimit(10000)
threading.stack_size(10**8)
t = threading.Thread(target=main)
t.start()
t.join()
