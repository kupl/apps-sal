def binary_search(x):

    low = 1
    high = 1.5 * 10**7
    while low < high:
        mid = (low + high) // 2

        l1 = mid * (mid + 1) // 2
        l2 = (mid + 1) * (mid + 2) // 2
        if x >= l1 and x < l2:
            return mid

        elif x < l1:
            high = mid
        else:
            low = mid + 1

    assert("error")


def solve(x):

    if x == 0:
        return 1

    n = binary_search(x)

    return int(x + 1 - n * (n + 1) // 2)


def __starting_point():

    x = int(input())
    print(solve(x - 1))


__starting_point()
