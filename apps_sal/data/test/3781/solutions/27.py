import sys
from functools import reduce
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if N % 2 == 1:
        print('Second')
    else:
        A.sort()
        for (a, na) in zip(A[::2], A[1::2]):
            if not a == na:
                break
        else:
            print('Second')
            continue
        print('First')
