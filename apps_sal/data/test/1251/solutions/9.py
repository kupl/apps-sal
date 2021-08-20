import sys
sys.setrecursionlimit(1000000)
n = int(input())
A = list(map(int, input().split()))


def Analyze(left, right, counted_height):
    if left >= right:
        return 0
    min_height = min(A[left:right])
    equinox = left + A[left:right].index(min_height)
    count_isHorizontal = min_height - counted_height
    count_isVertical = right - left
    return min(count_isVertical, count_isHorizontal + Analyze(left, equinox, min_height) + Analyze(equinox + 1, right, min_height))


print(Analyze(0, n, 0))
