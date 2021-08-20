import sys
input = sys.stdin.readline


def main():
    (a, b) = input().split()
    (c, d) = b.split('.')
    if len(d) == 1:
        d = d + '0'
    (p, q) = (int(a), int(c) * 100 + int(d))
    ans = p * q // 100
    print(ans)


def __starting_point():
    main()


__starting_point()
