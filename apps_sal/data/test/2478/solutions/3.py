import sys
input = sys.stdin.readline
from collections import deque


def read():
    N = int(input().strip())
    S = input().strip()
    return N, S


def solve(N, S):
    rank = 0
    q = deque()
    for s in S:
        if rank == 0:
            if s == ")":
                q.appendleft("(")
                q.append(")")
            else:
                q.append("(")
                rank += 1
        else:
            if s == ")":
                q.append(")")
                rank -= 1
            else:
                q.append("(")
                rank += 1
    while rank > 0:
        q.append(")")
        rank -= 1
    return "".join(q)


def __starting_point():
    inputs = read()
    print((solve(*inputs)))

__starting_point()
