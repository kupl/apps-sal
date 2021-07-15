# Contest No.: 645
# Problem No.: A
# Solver:      JEMINI
# Date:        20200526

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        if n * m % 2:
            print(n * m // 2 + 1)
        else:
            print(n * m // 2)
    return

def __starting_point():
    main()
__starting_point()
