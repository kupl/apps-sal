import math


def __starting_point():

    a, b = list(map(int, input().split()))

    if a == 0 and b == 0:
        print("NO")
    elif a == b or a + 1 == b or a == b + 1:
        print("YES")
    else:
        print("NO")


__starting_point()
