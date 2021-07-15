import sys

input = sys.stdin.readline


def main():
    n = int(input())
    result = False
    count = 0
    for _ in range(n):
        a, b = list(map(int, input().split()))
        if a == b:
            count += 1
        else:
            count = 0
        if count > 2:
            result = True

    print(("Yes" if result else "No"))


def __starting_point():
    main()

__starting_point()
