import math
import collections
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    oc = 0
    for i in a:
        oc += i % 2
    if oc:
        if oc % 2:
            print('YES')
        elif n - oc:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
