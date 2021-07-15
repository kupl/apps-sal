"""Codeforces Round #404 (Div. 2)

C. Anton and Fairy Tale
"""


def main():
    n, m = list(map(int, input().split()))

    if n <= m:
        print(n)
        return

    def func(k):
        return n + (k - m - 1) * m + ((m * (m + 1)) // 2) - ((k * (k + 1)) // 2)

    start, end = m + 1, n
    while start < end:
        middle = (start + end) // 2
        if func(middle) <= 0:
            end = middle
        else:
            start = middle + 1

    print(end)


def __starting_point():
    main()

__starting_point()
