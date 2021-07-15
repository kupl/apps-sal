from bisect import bisect, bisect_left


def bin_search(n):

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort()
    c.sort()

    ans = 0

    for i in range(n):
        upper_b = bisect_left(a, b[i])
        under_b = n - bisect(c, b[i])
        ans += upper_b * under_b
    return ans


def __starting_point():
    n = int(input())
    print((bin_search(n)))

__starting_point()
