import sys
import threading
import os.path
import collections
import heapq
import math
import bisect
import string
from platform import python_version
sys.setrecursionlimit(10 ** 6)
threading.stack_size(2 ** 27)


def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    n = int(input.readline())
    (lis, counter) = ([], 0)
    (rightc, leftc) = (0, 0)
    for i in range(n):
        (a, b) = list(map(int, input.readline().split()))
        if a == 0:
            rightc += 1
        if b == 0:
            leftc += 1
    counter = min(rightc, n - rightc) + min(leftc, n - leftc)
    output = counter
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


threading.Thread(target=main).start()
