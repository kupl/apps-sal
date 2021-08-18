

import fileinput


def test():
    pass


def __starting_point():
    n, p, k = list(map(int, input().split()))

    output = ""

    if p - k > 1:
        output = "<< "

    for i in range(p - k, p + k + 1):
        if i == p:
            output += "(" + str(i) + ") "
        elif i > n:
            break
        elif i > 0:
            output += str(i) + " "

    if p + k < n:
        output += ">>"

    print(output)


__starting_point()
