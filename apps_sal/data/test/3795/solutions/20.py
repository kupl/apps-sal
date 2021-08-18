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
    r = Read.int()
    d = Read.int()
    e = Read.int() * 5

    m = math.inf
    for i in range(r // e + 1):
        t = (r - i * e) % d
        if t < m:
            m = t
        if m == 0:
            print(0)
            return
    print(m)


query_count = 1
for j in range(query_count):
    solve()
