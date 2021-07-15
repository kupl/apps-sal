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
    n, k = Read.list_int()
    s = input()

    sf = 'RGB' * (k + 2)

    max_s = 0
    for i in range(n - k + 1):
        for j in range(3):
            count = 0
            for b in range(k):
                if sf[j + b] == s[i + b]:
                    count += 1
            if count > max_s:
                max_s = count

    print(k - max_s)


query_count = Read.int()
for j in range(query_count):
    solve()

