import math
import string
import random
from random import randrange
from collections import deque
from collections import defaultdict


def solve(n, arr):
    ans = 0

    st = 0
    while st < n and arr[st] == 0:
        st += 1

    ed = n - 1
    while ed >= 0 and arr[ed] == 0:
        ed -= 1

    if st == n or ed == -1:
        print(0)
        return

    for i in range(st, ed + 1):
        if arr[i] == 0:
            ans += 1

    print(ans)
    return


def main():
    t = int(input())
    while t > 0:
        t -= 1

        n = int(input())
        arr = list(map(int, input().strip().split(" ")))

        solve(n, arr)

    return


def test():
    arr_size = 25
    test_cases = 100
    min_range = -100
    max_range = 100
    str_size = 30
    step = 1

    for i in range(test_cases):
        k = []

        for j in range(arr_size):
            num = randrange(min_range, max_range, step)
            k.append(num)

        solve(n, arr)
        print("<-------- DEBUG ----------->")

    return


def __starting_point():
    main()


__starting_point()
