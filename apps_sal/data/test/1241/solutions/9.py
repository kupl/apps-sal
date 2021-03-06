import random
from collections import Counter, namedtuple
Array = namedtuple('Array', ['length', 'start', 'stop'])


def get_solution(n, k, input_list):
    array = Array(0, 0, 0)
    stop = 0
    zeros = 0
    for start in range(n):
        while stop < n:
            value = input_list[stop]
            length = stop - start + 1
            if value == 0:
                zeros += 1
            if zeros > k and value == 0:
                zeros -= 1
                break
            else:
                if array.length < length:
                    array = Array(length, start, stop + 1)
                stop += 1
        if input_list[start] == 0:
            zeros -= 1
        start += 1
    return array


def solve(n, k, input_list):
    solution = get_solution(n, k, input_list)
    if solution:
        (length, start, stop) = solution
        input_list[start:stop] = [1] * (stop - start)
        print(length)
    else:
        print(0)
    print(' '.join(map(str, input_list)))


def main():
    (n, k) = list(map(int, input().split()))
    input_list = list(map(int, input().split()))
    solve(n, k, input_list)


def __starting_point():
    main()


__starting_point()
