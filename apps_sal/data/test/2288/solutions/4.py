from bisect import bisect_left as lower_bound, bisect_right as upper_bound
from sys import stdin, stdout
from collections import defaultdict


def solve(arr, n):
    pass


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))

        if len(set(b)) == 1:
            if sorted(a) == a:
                print("Yes")
            else:
                print("No")

        else:
            print("Yes")


def __starting_point(): main()


__starting_point()
