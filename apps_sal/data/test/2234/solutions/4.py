import math


def main():
    (n, k) = list(map(int, input().split()))
    if k % 2 == n % 2:
        print(max(0, k - n))
    else:
        print(max(1, k - n))


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


'\n60, 61\n'
'\n'
__starting_point()
