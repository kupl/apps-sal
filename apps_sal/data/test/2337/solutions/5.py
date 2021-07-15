import sys
import math
import heapq
import random
import collections
import bisect
import datetime

def main():
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')

    n = list(map(int, input().strip().split()))
    l1 = list(map(int, input().strip().split()))
    l2 = list(map(int, input().strip().split()))
    count = 0

    for i in l1:
        pos = bisect.bisect_left(l2, i)

        if pos < len(l2) and l2[pos] >= i:
                l2 = l2[pos+1:]

        else:
            count = count + 1

    print(count)

    # sys.stdin.close()
    # sys.stdout.close()

def __starting_point():
    main()

__starting_point()
