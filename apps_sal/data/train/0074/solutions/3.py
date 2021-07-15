from typing import List
import sys
input = sys.stdin.readline
import math

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input().strip()
    return(list(s[:len(s)]))
def invr():
    return(list(map(int,input().strip().split())))



def solve_hungarian(a: List[List[int]], n: int, m: int):
    """
    Implementation of Hungarian algorithm in n^2 m
    """
    # potentials
    u = [0] * (n+1)
    v = [0] * (m+1)

    # pair row of each col
    p = [0] * (m+1)

    # for each col the number of prev col along the augmenting path
    way = [0] * (m+1)


    for i in range(1, n+1):
        p[0] = i
        j0 = 0
        minv = [float('inf')] *  (m+1)
        used = [False] * (m+1)

        # iterative Kun starts here
        condition = True
        while condition:
            # mark the current col as reachable
            used[j0] = True
            i0 = p[j0]
            delta = float('inf')

            # determine which col will become reachable after next potential update
            for j in range(1, m+1):
                if not used[j]:
                    cur = a[i0][j] - u[i0]-v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
                        # j1 will hold the col with min
                        # way[j1] - the prev col in dfs

            # update the potential
            for j in range(0, m+1):
                if used[j]: # if col j was discovered:
                    u[p[j]] += delta
                    v[j] -= delta
                else: # not discovered - update min?
                    minv[j] -= delta

            # j0 becomes the col on which the delta is achieved
            j0 = j1
            # p[j0] == 0 => j0 - a col not in matching
            condition = p[j0] != 0

        # the augmenting path was found - update the mapping
        condition = True
        while condition:

            # j1 is the prev column of j0 in augmenting path
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            condition = j0 != 0

    ans = [0] * (n+1)
    for j in range(1, m+1):
        ans[p[j]] = j

    return -v[0], ans


def solve(n, k, a, b):
    A = [[0] * (n+1) for _ in range(n+1) ]

    for i in range(1, n+1):
        for j in range(1, k+1):
            A[i][j] = a[i] + (j-1) * b[i]
        for j in range(k+1, n+1):
            A[i][j] = (k-1) * b[i]

        # turn into a max problem
    for i, row in enumerate(A):
        M = max(row)
        for j in range(n+1):
            A[i][j] = M - A[i][j]

    cost, match = solve_hungarian(A, n, n)

    print(n + (n-k))

    role_to_creature = list(zip(match, list(range(len(match)))))
    role_to_creature.sort()

    res = []

    for index in range(1, k):
        res.append(role_to_creature[index][1])

    for index in range(k+1, n+1):
        res.append(role_to_creature[index][1])
        res.append(-role_to_creature[index][1])
    res.append(role_to_creature[k][1])
    print(" ".join(map(str, res)))




def from_file(f):
    return f.readline


# with open('test.txt') as f:
#     input = from_file(f)
t = inp()
for _ in range(t):
    n, k = invr()
    a = [0]
    b = [0]
    for _ in range(n):
        ai, bi = invr()
        a.append(ai)
        b.append(bi)
    solve(n, k, a, b)






