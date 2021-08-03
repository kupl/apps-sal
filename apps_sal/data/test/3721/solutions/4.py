"""
https://codeforces.com/contest/1012/problem/B

"""
from sys import stdin, stdout


class UnionFind():
    def __init__(self, arr=[]):
        self.rank = {}
        self.leader = {}
        for i in arr:
            self.rank[i] = 0
            self.leader[i] = i

    def __repr__(self):
        return f""" Ranks : {self.rank}, leaders : {self.leader} """

    def find(self, x):
        leader = self.leader.get(x, x)
        if leader != x:
            leader = self.find(leader)
            self.leader[x] = leader
        return leader

    def getRank(self, x):
        return self.rank.get(x, 0)

    def union(self, x, y):
        leader1 = self.find(x)
        leader2 = self.find(y)
        if leader1 == leader2:
            return False
        if self.getRank(leader1) > self.getRank(leader2):
            self.leader[leader2] = leader1
        elif self.getRank(leader1) < self.getRank(leader2):
            self.leader[leader1] = leader2
        else:
            self.leader[leader1] = leader2
            self.rank[leader2] = 1 + self.getRank(leader2)
        return True


n, m, q = tuple(map(int, stdin.readline().split()))
uf = UnionFind(range(1, n + m + 1))
rcs = [tuple(map(int, line.split())) for line in stdin]
grps = n + m
for r, c in rcs:
    if uf.union(r, c + n):
        grps -= 1

stdout.write(str(grps - 1))
