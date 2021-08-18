import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))


def painting(left, right, arr, height):
    if left >= right:
        return 0

    min_height = min(arr[left:right])
    split = left + arr[left:right].index(min_height)

    count_horizontal = min_height - height
    count_vertical = right - left

    return min(count_vertical,
               count_horizontal + painting(left, split, arr, min_height) + painting(split + 1, right, arr, min_height))


print(painting(0, len(a), a, 0))
