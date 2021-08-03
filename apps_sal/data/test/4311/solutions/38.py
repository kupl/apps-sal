# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def func(n):
    ans = 0
    if n % 2 == 0:
        ans = n // 2
    else:
        ans = 3 * n + 1
    return ans


def main():
    s = int(input())
    dp = [s]
    counter = 0

    if s == 1 or s == 2:
        print(4)
        return

    while counter < 1000001:
        n = dp.pop()
        tmp = func(n)
        dp.append(n)
        dp.append(tmp)
        counter += 1
        if tmp == 4:
            print(dp.index(tmp) + 4)
            break


def __starting_point():
    main()


__starting_point()
