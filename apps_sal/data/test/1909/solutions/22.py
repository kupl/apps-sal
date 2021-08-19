# python3
import sys
import threading
import os.path
import collections
import heapq
import math
import bisect
import string

sys.setrecursionlimit(10 ** 6)
threading.stack_size(2 ** 27)


def main():
    if os.path.exists('in.txt'):
        input = open('in.txt', 'r')
    else:
        input = sys.stdin
    # --------------------------------INPUT---------------------------------
    n, k = list(map(int, input.readline().split()))
    lis = list(map(int, input.readline().split()))

    lis1 = [0 for i in range(k)]

    case1 = n / k
    ans1, ans2 = 10000000, 0
    for i, x in enumerate(lis):
        lis1[i % k] += lis[i]

    ans1 = min(lis1)
    for i, x in enumerate(lis1):
        if x == ans1:
            ans2 = i + 1
            break

    output = ans2
    # -------------------------------OUTPUT----------------------------------
    if os.path.exists('out.txt'):
        open('out.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


def __starting_point():
    main()
# threading.Thread(target=main).start()


__starting_point()
