import sys


def main():
    n, k = list(map(int, sys.stdin.readline().split()))
    if k == 0 or k == n:
        print(0, 0)
        return

    if k * 3 >= n:
        m = n - k
    else:
        m = 2 * k

    print(1, m)


main()
