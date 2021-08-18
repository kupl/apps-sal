import math


class Read:
    @staticmethod
    def string():
        return input()

    @staticmethod
    def int():
        return int(input())

    @staticmethod
    def list(sep=' '):
        return input().split(sep)

    @staticmethod
    def list_int(sep=' '):
        return list(map(int, input().split(sep)))


def solve():
    a, b = Read.list_int()
    if a == b:
        print(0)
    elif a > b:
        if (a - b) % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        if (b - a) % 2 == 1:
            print(1)
        else:
            print(2)


query_count = Read.int()
while query_count:
    query_count -= 1
    solve()
