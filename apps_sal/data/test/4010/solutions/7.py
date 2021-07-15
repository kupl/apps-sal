import sys
import math
import bisect

def solve(A):
    n = len(A)
    d = dict()
    for i in range(n):
        if A[i] not in d:
            d[A[i]] = i
        else:
            if i - d[A[i]] > 1:
                return True
    return False

def main():
    for _ in range(int(input())):
        n = int(input())
        A = list(map(int, input().split()))
        if solve(A):
            print('YES')
        else:
            print('NO')

def __starting_point():
    main()

__starting_point()
