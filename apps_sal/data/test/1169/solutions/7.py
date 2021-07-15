import sys
import os

def solve(n, m):
    if m == 0:
        return (n, n)
    minimum = max(0, n - m * 2)
    for i in range(1, n + 1):
        if i * (i - 1) // 2 >= m:
            return (minimum, n - i)

def main():
    n, m = (int(x) for x in input().split())
    print(' '.join(str(x) for x in solve(n, m)))

def __starting_point():
    main()
__starting_point()
