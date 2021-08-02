import math
import string
import random
from random import randrange
from collections import deque
from collections import defaultdict


def solve(n):
    ans = 0

    k = n % 10

    ans += 10 * (k - 1)

    f = len(str(n))

    for i in range(1, f + 1):
        ans += i

    print(ans)
    return


def main():
    t = int(input())
    while t > 0:
        t -= 1

        n = int(input())
        # s = input().strip()
        # x,y = map(int, input().strip().split(" "))
        # arr = list(map(int, input().strip().split(" ")))

        solve(n)

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
        # s = ''.join(random.choices(string.ascii_lowercase, k = str_size))

        for j in range(arr_size):
            num = randrange(min_range, max_range, step)
            k.append(num)

        solve(n, arr)
        print("<-------- DEBUG ----------->")

    return


def __starting_point():
    main()
    # test()


__starting_point()
