import math
import sys


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
    (n, T) = Read.list_int()
    a = Read.list_int()
    tmp = {}
    res = []
    for i in a:
        v = T - i
        r = '1'
        if v in tmp:
            if tmp[v] == '1':
                r = '0'
        tmp[i] = r
        res.append(r)
    print(' '.join(res))


query_count = Read.int()
while query_count:
    query_count -= 1
    solve()
