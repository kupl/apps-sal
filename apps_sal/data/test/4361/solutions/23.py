# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def ngram(numbers, n):
    return list([numbers[i:i + n] for i in range(len(numbers) - 2)])


def main():
    numbers = []
    n, m = map(int, input().split())
    [numbers.append(int(input())) for _ in range(n)]
    numbers.sort()
    print(min(numbers[i + m - 1] - numbers[i] for i in range(n - m + 1)))


def __starting_point():
    main()


__starting_point()
