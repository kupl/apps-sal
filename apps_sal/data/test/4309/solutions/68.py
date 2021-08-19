import sys
import math
sys.setrecursionlimit(500000)
INF = float('inf')


def main():
    n = int(input())
    for i in range(n, 1000):
        flag = True
        for (j, c) in enumerate(str(i)):
            if j == 0:
                continue
            elif c != str(i)[0]:
                flag = False
                break
        if flag:
            return i


def __starting_point():
    print(main())


__starting_point()
