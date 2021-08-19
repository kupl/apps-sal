import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    (N, K) = list(map(int, input().split()))
    if K % 2 == 1:
        a = N // K
        print(a * a * a)
        return
    else:
        a = N // K
        count = a * a * a
        b = (N + K // 2) // K
        count += b * b * b
        print(count)


def __starting_point():
    main()


__starting_point()
