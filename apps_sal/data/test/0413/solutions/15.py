def main() -> object:
    """

    :rtype : Integer
    :return: The answer which the problem is required.
    """
    n, m = [int(i) for i in input().split()]
    count = 0
    while n < m:
        if m % 2 == 0:
            m >>= 1
        else:
            m += 1
        count += 1
    count += n - m
    return count

def __starting_point():
    print(main())
__starting_point()
