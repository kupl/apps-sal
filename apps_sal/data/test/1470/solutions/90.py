import bisect
import itertools
import math
import random
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import xor

mod = 10 ** 9 + 7


def lmi():
    return list(map(int, input().split()))


def main():
    x = int(input())
    ans = x // 11 * 2
    ans += math.ceil((x % 11) / 6)
    print(ans)


def __starting_point():
    main()


__starting_point()
