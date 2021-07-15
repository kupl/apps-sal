import sys
input = sys.stdin.readline


def main():
    N = int(input())
    L = list(map(int, input().split()))

    if max(L) < sum(L) - max(L):
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
