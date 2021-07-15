import sys
import os

def solve(s):
    n = len(s)
    for i in range(n // 2):
        a = ord(s[i])
        b = ord(s[n - 1 - i])
        diff = abs(a - b)
        if diff != 0 and abs(diff) != 2:
            return 'NO'
    return 'YES'

def main():
    t = int(input())
    for i in range(t):
        _ = int(input())
        s = input()
        print(solve(s))


def __starting_point():
    main()
__starting_point()
