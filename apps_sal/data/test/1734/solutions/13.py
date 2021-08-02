"""
-----------------------------Pseudo---------------------------------
"""
import sys
from collections import defaultdict
def input(): return sys.stdin.readline()


def print(arg, *argv, end=None):
    sys.stdout.write(str(arg))
    for i in argv:
        sys.stdout.write(" " + str(i))
    sys.stdout.write(end) if end or end == "" else sys.stdout.write("\n")


def mapi(): return map(int, input().split())
def maps(): return map(str, input().split())
#---------------------------------------------------------------#


def solve():
    t = 1
    #t = int(input())
    for _ in range(t):
        n = int(input())
        ss = []
        a = []
        mem = defaultdict(int)
        for __ in range(n):
            x = input().strip()
            a.append(x)
            sett = set()
            for i in range(9):
                for j in range(i + 1, 10):
                    sett.add(x[i:j])
            for it in sett:
                mem[it] += 1

        for id in range(n):
            length = 1
            flag = True
            while length < 10 and flag:
                i = 0
                j = length
                while i < 9 and j < 10:
                    tmp = a[id][i:j]
                    if mem[tmp] == 1:
                        print(tmp)
                        flag = False
                        break
                    i += 1
                    j += 1
                length += 1

#---------------------------------------------------------------#


def __starting_point():
    solve()


__starting_point()
