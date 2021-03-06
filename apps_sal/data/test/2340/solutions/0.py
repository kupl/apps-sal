import sys
import math
from collections import defaultdict
from itertools import combinations
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


def read():
    return list(map(int, input().split()))


def write(*args, sep='\n'):
    for i in args:
        sys.stdout.write('{}'.format(i) + sep)


INF = float('inf')
MOD = int(1000000000.0 + 7)
for q in range(int(input())):
    (h, n) = read()
    arr = list(read()) + [0]
    if n == 1:
        write(0)
        continue
    ans = 0
    cur = h
    for i in range(1, n):
        if cur == arr[i]:
            continue
        elif arr[i + 1] == arr[i] - 1:
            cur = arr[i] - 1
        else:
            ans += 1
    write(ans)
