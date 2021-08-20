import math
import collections
a = collections.OrderedDict()


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        t = tuple([int(x) for x in input().split()])
        result = None
        occ = dict()
        for k in range(len(t)):
            ele = t[k]
            if ele in occ:
                new_result = k - occ[ele] + 1
                if result is None or new_result < result:
                    result = new_result
            occ[ele] = k
        if result is None:
            print(-1)
        else:
            print(result)


def __starting_point():
    main()


__starting_point()
