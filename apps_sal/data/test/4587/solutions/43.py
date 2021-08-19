import copy
import math
import time
import statistics
import math
import itertools
import bisect


def get_int():
    return int(input())


def get_string():
    return input()


def get_int_list():
    return [int(x) for x in input().split()]


def get_string_list():
    return input().split()


def get_int_multi():
    return list(map(int, input().split()))


def get_string_char_list():
    return list(str(input()))


'\nwhile (idx < n) and ():\n\n    idx += 1\n'


def main():
    start = time.time()
    n = get_int()
    a_list = get_int_list()
    b_list = get_int_list()
    c_list = get_int_list()
    a_list.sort()
    b_list.sort()
    c_list.sort()
    a_count = []
    b_count = []
    b_count2 = []
    idx = 0
    for a in a_list:
        idx = bisect.bisect_right(b_list, a, idx)
        a_count.append(idx)
    idx = 0
    for b in b_list:
        idx = bisect.bisect_right(c_list, b, idx)
        b_count.append(idx)
    ruikei = 0
    for i in range(n - 1, -1, -1):
        ruikei += n - b_count[i]
        b_count2.append(ruikei)
    b_count2.sort(reverse=True)
    ans = 0
    for a in a_count:
        if a == n:
            continue
        ans += b_count2[a]
    print(ans)


def __starting_point():
    main()


__starting_point()
