import sys
import os


def solve(stages, k):
    s = dict()
    for char in stages:
        s[ord(char) - ord('a')] = True

    weight = 0
    current = 0
    last = -2
    for i in range(26):
        if i in s:
            if i >= last + 2:
                weight += i + 1
                current += 1
                last = i

        if current == k:
            break

    return -1 if current < k else weight

def main():
    n, k = map(int, input().split())
    stages = input()
    print(solve(stages, k))

def __starting_point():
    main()
__starting_point()
