def main():
    from itertools import accumulate
    from collections import Counter
    print(int(input()) - Counter(accumulate(list(map(int, input().split())))).most_common()[0][1])


def __starting_point():
    main()

__starting_point()
