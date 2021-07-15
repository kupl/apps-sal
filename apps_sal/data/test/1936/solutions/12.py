# Contest No.: Edu92
# Problem No.: A
# Solver:      JEMINI
# Date:        20200729

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        if b < 2 * a:
            print(-1, -1)
        else:
            print(a, 2 * a)



    return

def __starting_point():
    main()
__starting_point()
