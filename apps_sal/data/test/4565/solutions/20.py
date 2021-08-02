from itertools import accumulate
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    n = int(input())
    s = list(input())
    enum = [1 if c == 'E' else 0 for c in s]
    wnum = [1 if c == 'W' else 0 for c in s]
    enuma = tuple(accumulate(enum))
    wnuma = tuple(accumulate(wnum))
    wnumm = wnuma[-1]
    wnuma2 = [wnumm - wn for wn in wnuma]
    num = max(wnuma2[0], enuma[-2])
    for i1 in range(1, n - 1):
        num = max(num, enuma[i1 - 1] + wnuma2[i1])
    r = n - num - 1
    print(r)


def __starting_point():
    main()


__starting_point()
