import sys
import math


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def MI():
    return map(int, sys.stdin.readline().split())


def SI():
    return sys.stdin.readline().strip()


t = II()
for q in range(t):
    s = SI()
    ans = ''
    d = {'R': 'P', 'S': 'R', 'P': 'S'}
    m = 0
    if s.count('R') > m:
        m = s.count('R')
        ans = 'R'
    if s.count('S') > m:
        m = s.count('S')
        ans = 'S'
    if s.count('P') > m:
        ans = 'P'
    ans = d[ans]
    print(ans * len(s))
