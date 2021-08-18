from bisect import bisect_right
from bisect import bisect_left
from collections import defaultdict
from math import sqrt, factorial, gcd, log2, inf, ceil
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    count = 0
    i = 0
    while i < n:
        if l1[i] != l2[i]:
            j = i

            count += 1
            if count == 2:
                break
            seti = set()
            while l1[j] != l2[j]:
                seti.add((l2[j] - l1[j]))
                j += 1
                if j == n:
                    break
            i = j
            if j == n:
                break

        else:
            i += 1

    if count == 1:
        if len(seti) == 1:
            z = seti.pop()
            if z > 0:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    elif count == 0:
        print('YES')

    else:
        print('NO')
