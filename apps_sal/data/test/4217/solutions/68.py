# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    interview = []
    n, m = map(int, input().split())
    interview = [list(map(int, input().split())) for _ in range(n)]
    set_data = {}

    for data in interview:
        if len(set_data) == 0:
            set_data = set(data[1:])
        else:
            set_data = set_data & set(data[1:])
    print(len(set_data))


def __starting_point():
    main()


__starting_point()
