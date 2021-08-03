# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    people = []
    d, x = map(int, input().split())
    people = list([int(input()) for _ in range(n)])
    chocolates = []
    choco = 1

    for human in people:
        for day in range(1, d + 1):
            if d >= human * day + 1:
                choco += 1
        chocolates.append(choco)
        choco = 1
    print(sum(chocolates) + x)


def __starting_point():
    main()


__starting_point()
