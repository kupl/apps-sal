import sys


def fast_input():
    return sys.stdin.readline().strip()


def data_input():
    return [int(x) for x in fast_input().split()]


def binary_search(array, x):
    left, right = -1, len(array)
    while left + 1 != right:
        middle = (left + right) // 2
        if array[middle] >= x:
            right = middle
        elif array[middle] < x:
            left = middle
    return right


def solve_of_problem():
    a, b = data_input()
    if (b - a) % 2 == 1 and a < b:
        print(1)
    elif (b - a) % 2 == 0 and b < a:
        print(1)
    elif a == b:
        print(0)
    else:
        print(2)
    return


for ______ in range(int(fast_input())):
    solve_of_problem()
