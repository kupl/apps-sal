from collections import defaultdict, deque, Counter, OrderedDict
from math import gcd


def main():
    n = int(input())
    g, d = 0, set()
    for i in map(int, input().split()):
        if g == 0:
            g = i
        else:
            g = gcd(g, i)
        d.add(i)
    print(g if g in d else -1)


def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)
    thread = threading.Thread(target=main)
    thread.start()"""
    main()


__starting_point()
