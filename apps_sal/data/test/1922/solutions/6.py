import sys
pin = sys.stdin.readline


def main():
    (N, M) = map(int, pin().split())
    print(abs((N - 2) * (M - 2)))
    return


main()
