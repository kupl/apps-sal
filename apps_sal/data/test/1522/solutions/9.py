import sys
import collections


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    more_keys = 0
    keys = collections.Counter()
    for i, x in enumerate(s):
        if i % 2 == 0:
            keys[x] += 1
        else:
            k = x.lower()
            if keys[k] > 0:
                keys[k] -= 1
            else:
                more_keys += 1
    print(more_keys)


def __starting_point():
    main()


__starting_point()
