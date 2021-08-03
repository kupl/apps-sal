from typing import List
from collections import deque
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(list(map(int, input().split())))


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
            #print(f"Skipped as grey")
            return

        if ineib == m - 1:
            # no need to wait there
            states[ineib][gneib] = states[index][g_left]
            #print(f"Final state dist is {states[ineib][gneib]}")

        elif gneib == 0:
            states[ineib][gneib] = states[index][g_left] + 1
            states[ineib][g] = states[ineib][gneib]
            gneib = g
            q.append((ineib, gneib))
            #print(f"appended right with distance {states[ineib][0]}")
        else:
            states[ineib][gneib] = states[index][g_left]
            q.appendleft((ineib, gneib))

    while q:
        # sit for this is known
        #print(f"Queue is {[(A[i], t) for i,t in q]}")
        index, g_left = q.popleft()
        #print(f"Popped {A[index], g_left}. Dist is {states[index][g_left]}")

        #neib = get_neib(index, g_left, A)
        #print(f"Neighbors are {[(A[i], t) for i, t in neib]}")

        if index > 0:
            # there exists a next one
            delta = A[index] - A[index - 1]
            if g_left >= delta:
                process_neib(index - 1, g_left - delta)

        if index < m - 1:
            delta = A[index + 1] - A[index]
            if g_left >= delta:
                process_neib(index + 1, g_left - delta)

                #print(f"appended left with distance {states[ineib][gneib]}")

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


# with open('52.txt') as f:
#     input = from_file(f)
n, m = invr()
A = inlt()
g, r = invr()
compute(n, m, g, r, A)
