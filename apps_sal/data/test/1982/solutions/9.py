import sys
import math
import bisect

def solve(n, k):
    m = k ** 2
    return n >= m and (n - m) % 2 == 0

def main():
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        if solve(n, k):
            print('YES')
        else:
            print('NO')

def __starting_point():
    main()

__starting_point()
