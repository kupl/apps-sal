import sys
import threading
import os.path
import collections
import heapq
import math
import bisect
import string
from platform import python_version
import itertools
sys.setrecursionlimit(10**6)
threading.stack_size(2**27)


def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    n, q = list(map(int, input.readline().split()))
    lis = list(map(int, input.readline().split()))
    lis.sort()
    val = [0] * (n + 1)
    for i in range(q):
        l, r = list(map(int, input.readline().split()))
        val[l - 1] += 1
        val[r] -= 1
    for i in range(n):
        val[i + 1] += val[i]
    val.sort()
    sum = 0
    for i in range(n):
        sum += val[i + 1] * lis[i]
    output = sum
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


def __starting_point():
    main()


__starting_point()
