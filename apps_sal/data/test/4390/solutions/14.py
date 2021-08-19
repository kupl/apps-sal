from sys import stdin, stdout
import sys
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        (a, b) = [int(s) for s in input().split()]
        w = a // b
        w1 = a % b
        if w1 == 0:
            print(0)
        else:
            print(b - w1)


def __starting_point():
    main()


__starting_point()
