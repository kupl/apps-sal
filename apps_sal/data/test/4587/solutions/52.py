import sys
from math import factorial
MOD = 10 ** 9 + 7
INF = 10000000000


def binary_search_section(list, min, max):
    low = 0
    high = len(list) - 1
    upper = len(list)
    lower = -1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess >= min:
            high = mid - 1
        else:
            low = mid + 1
            lower = mid
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess > max:
            high = mid - 1
            upper = mid
        else:
            low = mid + 1
    return [lower, upper]


def main():
    n = int(input())
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))
    cList = list(map(int, input().split()))
    aListSorted = sorted(aList)
    bListSorted = sorted(bList)
    cListSorted = sorted(cList)
    result = 0
    for b in bListSorted:
        sec = binary_search_section(aListSorted, aListSorted[0], b - 1)
        sec2 = binary_search_section(cListSorted, b + 1, cListSorted[-1])
        result += (sec[1] - sec[0] - 1) * (sec2[1] - sec2[0] - 1)
    print('{}'.format(result))


def __starting_point():
    main()


__starting_point()
