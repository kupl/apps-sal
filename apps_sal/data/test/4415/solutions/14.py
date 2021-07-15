# -*- coding: utf-8 -*-


def __starting_point():
    _ = int(input())

    array = sorted(list(map(int, input().split())))
    inc = []
    dec = []
    for elem in array:
        if elem in inc[-1:] and elem in dec[-1:]:
            inc = None
            dec = None
            break;

        if elem in inc[-1:]:
            dec.append(elem)
        else:
            inc.append(elem)

    if inc is None:
        print("NO")
    else:
        print("YES")
        print(len(inc))
        print(" ".join(str(e) for e in inc))
        print(len(dec))
        print(" ".join(str(e) for e in dec[::-1]))

__starting_point()
