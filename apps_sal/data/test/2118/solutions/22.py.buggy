import random
import math
from copy import deepcopy as dc

calls = 1

# Function to call the actual solution


def solution(n, k):
    if k % 2 == 0 or k > (2 * n) - 1:
        return -1
    li = [i for i in range(1, n + 1)]

    def mergeCount(li, s, e, k):
        nonlocal calls
        if calls >= k or s >= e - 1:
            return
        mid = (s + e) // 2
        calls += 2
        if mid - 1 >= s:
            li[mid], li[mid - 1] = li[mid - 1], li[mid]
            mergeCount(li, s, mid, k)
            mergeCount(li, mid, e, k)
    mergeCount(li, 0, n, k)
    return li


# Function to take input
def input_test():
    n, k = list(map(int, input().strip().split(" ")))
    out = solution(n, k)
    if out != -1:
        print(' '.join(list(map(str, out))))
    else:
        print(out)


input_test()
# test()s
