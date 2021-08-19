# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main2():
    numbers = []
    n, m = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(m)]
    dp = [0] * n
    for number in numbers:
        for n in number:
            dp[n - 1] += 1
    for ans in dp:
        print(ans)


def main():
    numbers = []
    n, m = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(m)]
    dp = {}
    for number in numbers:
        for n in number:
            if n not in dp:
                dp[n] = 1
            else:
                dp[n] += 1
    print(dp)
    for i in range(1, len(dp) + 1):
        print(dp[i])


def __starting_point():
    main2()


__starting_point()
