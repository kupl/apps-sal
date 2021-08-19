import math


class Read:

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
    (a, b, c) = Read.list_int()
    print((a + b + c) // 2)


query_count = Read.int()
for j in range(query_count):
    solve()
