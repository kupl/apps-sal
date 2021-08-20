from typing import List
from collections import deque
import sys
input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s) - 1])


def invr():
    return list(map(int, input().split()))


def compute(n, m, g, r, A: List[int]):
    A.sort()
    WHITE = -1
    GREY = -2
    states = [[WHITE] * (g + 1) for _ in range(m)]
    states[0][g] = 0
    states[0][0] = 0
    q = deque([(0, g)])

    def process_neib(ineib, gneib):
        if states[ineib][gneib] != WHITE:
            return
        if ineib == m - 1:
            states[ineib][gneib] = states[index][g_left]
        elif gneib == 0:
            states[ineib][gneib] = states[index][g_left] + 1
            states[ineib][g] = states[ineib][gneib]
            gneib = g
            q.append((ineib, gneib))
        else:
            states[ineib][gneib] = states[index][g_left]
            q.appendleft((ineib, gneib))
    while q:
        (index, g_left) = q.popleft()
        if index > 0:
            delta = A[index] - A[index - 1]
            if g_left >= delta:
                process_neib(index - 1, g_left - delta)
        if index < m - 1:
            delta = A[index + 1] - A[index]
            if g_left >= delta:
                process_neib(index + 1, g_left - delta)
    res = float('inf')
    for g_left in range(g):
        if states[m - 1][g_left] >= 0:
            res = min(res, states[m - 1][g_left] * (r + g) + g - g_left)
    if res != float('inf'):
        print(res)
    else:
        print('-1')


def from_file(f):
    return f.readline


(n, m) = invr()
A = inlt()
(g, r) = invr()
compute(n, m, g, r, A)
