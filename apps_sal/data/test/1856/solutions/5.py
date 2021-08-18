import sys
import os
3


def main():
    N = read_int()
    S = [inp() for _ in range(N)]
    print(solve(N, S))


class Node(object):
    def __init__(self, v):
        self.v = v
        self.p = self

    def union(self, other):
        r1 = self.find()
        r2 = other.find()
        if r1 is not r2:
            r1.p = r2

    def find(self):
        r = self
        while r.p != r:
            r = r.p
        n = self
        while n.p != n:
            p = n.p
            n.p = r
            n = p
        return r


def solve(N, S):
    letters = [None] * 26
    nodes = [Node(i) for i in range(N)]
    orda = ord('a')
    for i in range(N):
        s = S[i]
        b = [False] * 26
        for c in s:
            b[ord(c) - orda] = True
        for j in range(26):
            if b[j]:
                if letters[j] is None:
                    letters[j] = nodes[i]
                else:
                    nodes[i].union(letters[j])

    ns = set()
    for n in nodes:
        ns.add(n.find().v)
    return len(ns)


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()


__starting_point()
