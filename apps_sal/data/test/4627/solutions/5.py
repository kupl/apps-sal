import copy
import sys
from collections import defaultdict as dd


def eprint(*args):
    print(*args, file=sys.stderr)


zz = 1
if zz:
    input = sys.stdin.readline
else:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('all.txt', 'w')


def li():
    return [int(x) for x in input().split()]


def fi():
    return int(input())


def si():
    return list(input().rstrip())


def mi():
    return map(int, input().split())


def bo(i):
    return ord(i) - ord('a')


t = fi()
while t > 0:
    t -= 1
    n = fi()
    a = li()
    d = {}
    o = e = 0
    for i in a:
        if i % 2:
            o += 1
        else:
            e += 1
        d[i] = 1
    if o % 2 == 0:
        print("YES")
        continue
    flag = 0
    for i in a:
        if i + 1 in d or i - 1 in d:
            print("YES")
            flag = 1
            break
    if flag == 0:
        print("NO")
