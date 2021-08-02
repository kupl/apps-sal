#!/user/bin/env pypy3
import sys
from typing import List


def fast_input():
    return sys.stdin.readline()[:-1]


def solve(mochi_list: List[int]) -> int:
    sorted_mochi_list = sorted(mochi_list)
    kagamimochi = set(sorted_mochi_list)
    return len(kagamimochi)


def main():
    n = int(fast_input())
    d = []
    for i in range(n):
        d.append(int(fast_input()))
    result = solve(d)
    print(result)


main()
