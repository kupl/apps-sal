import heapq
import sys
input = sys.stdin.readline


def main():
    numbers = []
    n = int(input())
    [numbers.append(int(input().rstrip())) for _ in range(n)]
    max_n = 0
    second_n = 0
    for i in numbers:
        if i > max_n:
            max_n = i
        elif i > second_n:
            second_n = i
    for i in numbers:
        if i == max_n:
            print(second_n)
        else:
            print(max_n)


def __starting_point():
    main()


__starting_point()
