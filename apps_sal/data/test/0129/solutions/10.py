import math


def __starting_point():
    (n, m, k, l) = list(map(int, input().split()))
    one_friend = (k + l) // m + int((k + l) % m != 0)
    if one_friend * m > n:
        print(-1)
    else:
        print(one_friend)


__starting_point()
