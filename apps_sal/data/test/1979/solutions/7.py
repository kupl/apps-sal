from bisect import bisect_left as lower_bound, bisect_right as upper_bound
from sys import stdin, stdout
from collections import defaultdict


def solve(arr, n):
    pass


def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    ma = {i: [] for i in range(1, n + 1)}
    for (index, num) in enumerate(a):
        ma[num].append(index)
    for (index, num) in enumerate(b):
        ma[num].append(index)
    cnt = {}
    ret = 0
    for i in range(1, n + 1):
        diff = ma[i][1] - ma[i][0]
        if diff < 0:
            diff = n - abs(diff)
        cnt[diff] = cnt.get(diff, 0) + 1
        ret = max(ret, cnt[diff])
    print(ret)


def __starting_point():
    main()


__starting_point()
