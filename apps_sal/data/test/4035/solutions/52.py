# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    numbers = []
    a, b = map(int, input().split())

    tmp1 = int(a / 0.08)
    tmp2 = int(b / 0.10)

    ans = []

    for i in range(min(tmp1, tmp2), max(tmp1, tmp2) + 2):
        if int(i * 0.08) == a and int(i * 0.10) == b:
            ans.append(i)

    if len(ans) > 0:
        print(min(ans))
    else:
        print("-1")


def __starting_point():
    main()


__starting_point()
