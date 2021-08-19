from collections import defaultdict
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    s = tuple(map(int, input()))
    lens = len(s)
    d1 = defaultdict(int)
    ss = 0
    num10 = 1
    for se in s[::-1]:
        ss += int(se) * num10 % 2019
        ss = ss % 2019
        d1[ss] += 1
        num10 = num10 * 10 % 2019
    r = d1[0]
    for v in d1.values():
        r += v * (v - 1) // 2
    print(r)


def __starting_point():
    main()


__starting_point()
