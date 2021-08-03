def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())

    l = 1
    r = n + 1

    while r - l != 1:
        m = l + r >> 1
        candies = m * (m + 1) // 2
        eat = n - m

        if candies - eat <= k:
            l = m
        else:
            r = m

    print(n - l)

    return 0


main()
