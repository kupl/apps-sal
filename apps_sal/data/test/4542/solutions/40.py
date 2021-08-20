import os
import sys
from itertools import groupby


def main():
    S = input()
    sgroup = groupby(S)
    for (cnt, (key, group)) in enumerate(sgroup):
        pass
    print(cnt)


def __starting_point():
    main()


__starting_point()
