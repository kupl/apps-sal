from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def input_nums():
    return list(map(int, input().split()))


def main():
    K = int(input())
    runrun_lst = []

    def rec(num_of_digit, runrun_val):
        runrun_lst.append(runrun_val)
        if num_of_digit == 10:
            return
        for i in range(-1, 2):
            add = runrun_val % 10 + i
            if 0 <= add <= 9:
                rec(num_of_digit + 1, runrun_val * 10 + add)
    for v in range(1, 10):
        rec(1, v)
    runrun_lst.sort()
    print(runrun_lst[K - 1])


def __starting_point():
    main()


__starting_point()
