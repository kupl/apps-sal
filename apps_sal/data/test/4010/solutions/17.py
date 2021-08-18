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


result = math.inf


def solve():
    n = Read.int()
    a = Read.list_int()
    for i in range(n):
        for j in range(i + 2, n):
            if a[i] == a[j]:
                print('YES')
                return
    print('NO')


query_count = Read.int()
while query_count:
    query_count -= 1
    solve()
