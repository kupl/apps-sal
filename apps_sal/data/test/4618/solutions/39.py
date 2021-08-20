import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    s = list(input())
    k = int(input())
    subs = set()
    lens = len(s)
    for i1 in range(k + 1):
        for i2 in range(lens - i1):
            subs.add(''.join(s[i2:i2 + i1 + 1]))
    subs_l = list(subs)
    subs_l.sort()
    print(subs_l[k - 1])


def __starting_point():
    main()


__starting_point()
