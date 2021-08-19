"""
NTC here
"""
from sys import stdin


def iin():
    return int(stdin.readline())


def lin():
    return list(map(int, stdin.readline().split()))


class Disjoint_set:

    class node:

        def __init__(self, a):
            self.value = a
            self.p = self
            self.rank = 0

    def __init__(self, a):
        self.data = {i: self.make_set(i) for i in range(1, a + 1)}

    def make_set(self, val):
        return self.node(val)

    def union(self, x, y):
        self.link(self.find_set(self.data[x]), self.find_set(self.data[y]))

    def link(self, val1, val2):
        if val1.rank > val2.rank:
            val2.p = val1
            val1.rank += 1
        else:
            val1.p = val2
            val2.rank += 1

    def find_set(self, val):
        if val.p.value != val.value:
            val.p = self.find_set(val.p)
        return val.p

    def solution(self):
        pr = {}
        parent = {}
        for i in self.data:
            vl = self.find_set(self.data[i]).value
            parent[i] = vl
            if vl in pr:
                pr[vl] += 1
            else:
                pr[vl] = 1
        return pr


def main():
    n = iin()
    s = [''.join(list(set(input()))) for i in range(n)]
    adj = [[] for _ in range(26)]
    s = list(set(s))
    l = len(s)
    for (k, i) in enumerate(s):
        for j in i:
            adj[ord(j) - ord('a')].append(k + 1)
    ds = Disjoint_set(l)
    done = set()
    for i in range(26):
        if adj[i]:
            x = adj[i][0]
            for j in adj[i]:
                if x != j and (x, j) not in done and ((j, x) not in done):
                    ds.union(x, j)
                    done.add((x, j))
    sl = ds.solution()
    print(len(sl))


main()
