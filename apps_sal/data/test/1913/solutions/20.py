
from sys import stdin
from collections import defaultdict
from operator import itemgetter


def main():
    n = int(stdin.readline())
    xs = stdin.readline().split()
    print("{}".format(run(xs)))


def run(xs):
    zeros = 0
    s = "1"
    for x in xs:
        if x == "0":
            return 0
        if beautiful(x):
            zeros += len(x) - 1
        else:
            s = x
    return s + "0" * zeros


def beautiful(s):
    found = False
    for c in s:
        if c == '0':
            pass
        elif c == '1':
            if found:
                return False
            else:
                found = True
        else:
            return False
    return True


def __starting_point():
    main()


__starting_point()
