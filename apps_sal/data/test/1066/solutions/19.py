import sys


def main():
    (n, k) = list(map(int, sys.stdin.readline().split()))
    max_odd_pos = int(n / 2)
    if n % 2 == 1:
        max_odd_pos += 1
    if k <= max_odd_pos:
        print(k * 2 - 1)
    else:
        print((k - max_odd_pos) * 2)


def __starting_point():
    return main()


__starting_point()
