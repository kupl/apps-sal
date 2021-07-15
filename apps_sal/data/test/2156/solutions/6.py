# Binary Indexed Tree (Fenwick Tree)
class BIT():
    def __init__(self, n):
        '''n = 要素数
        要素の添字iは 0 <= i < n となる
        '''
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        '''i番目の要素にvalを加算する O(logN)'''
        i = i + 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sum(self, i, j):
        '''区間[i, j)の和を求める O(logN)'''
        return self._sum(j) - self._sum(i)


import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
q = int(input())
query = [list(map(int, input().split())) for i in range(q)]

bit = BIT(n)
for i in range(n):
    bit.add(i, a[i])
for i in range(q):
    l, r = query[i]
    l -= 1
    print(bit.sum(l, r) // 10)


