from array import array
from bisect import bisect_right as bisect


def solve(nums):
    nums = array('l', nums)
    full_sum = sum(nums)
    (third, modulo) = divmod(full_sum, 3)
    two_thirds = third * 2
    if modulo:
        return 0
    a = array('l')
    b = array('l')
    len_nums_m2 = len(nums) - 2
    len_nums_m1 = len(nums) - 1
    accum = 0
    for (i, n) in enumerate(nums, 1):
        accum += n
        if accum == third and i <= len_nums_m2:
            a.append(i)
        if accum == two_thirds and 1 < i <= len_nums_m1:
            b.append(i)
    len_b = len(b)
    result = 0
    for n in a:
        subsize_b = len_b - bisect(b, n)
        result += subsize_b
    return result


def __starting_point():
    _ = int(input())
    nums = list(map(int, input().split()))
    answer = solve(nums)
    print(answer)


__starting_point()
