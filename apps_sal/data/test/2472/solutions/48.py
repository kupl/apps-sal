import os
import sys


def main():
    n = int(input())
    S = []
    for _ in range(n):
        S.append(list(map(int, input().split())))
    S.sort(key=lambda x: x[1])
    current_time = 0
    for s in S:
        current_time += s[0]
        if current_time <= s[1]:
            pass
        else:
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
