# -*-coding:utf-8-*-
import decimal
import sys
input = sys.stdin.readline


def main():
    numbers = []
    n = int(input())
    t, a = map(int, input().split())
    numbers = list(map(int, input().split()))
    dp = []
    hensu = decimal.Decimal('0.006')
    for number in numbers:
        tmp = abs(t - number * hensu - a)
        dp.append(tmp)
    answer = dp.index(min(dp)) + 1
    print(answer)


def __starting_point():
    main()


__starting_point()
