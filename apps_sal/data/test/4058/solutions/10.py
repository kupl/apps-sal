"""input
5 10
0 0 0 0 0
"""
from sys import stdin, stdout


def right_index_search(i, arr, k):
    j = i
    index = -1
    while j < len(arr) and j < i + k:
        if arr[j] == 1:
            index = j
        j += 1
    return index


def left_index_search(i, arr, k):
    j = i - 1
    index = -1
    while j >= 0 and j > i - k:
        if arr[j] == 1:
            index = j
            break
        j -= 1
    return index


def pylons(k, arr):
    count = 0
    i = 0
    while i < len(arr):
        index_right = right_index_search(i, arr, k)
        if index_right == -1:
            index_left = left_index_search(i, arr, k)
            if index_left == -1:
                return -1
            else:
                i = index_left + k
                count += 1
        else:
            i = index_right + k
            count += 1
    return count


def __starting_point():
    (n, k) = input().strip().split(' ')
    (n, k) = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pylons(k, arr)
    print(result)


__starting_point()
