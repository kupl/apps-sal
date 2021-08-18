import math
n, k = [int(i) for i in input().split()]
woods = [int(i) for i in input().split()]


def k_cut_less_than(k, l, woods):
    kaisuu = 0
    for wood in woods:
        kaisuu += (wood - 1) // l
    if kaisuu <= k:
        return False
    return True


def binary_research(start, end, function):
    if start == end:
        return start
    middle = math.ceil((start + end) / 2)
    if function(k, middle, woods):
        start = middle
    else:
        end = middle - 1
    return binary_research(start, end, function)


start = 0
end = 10**9
print((binary_research(start, end, k_cut_less_than) + 1))
