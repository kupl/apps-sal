from itertools import groupby


def isSolved(c):
    cons = [x[0] for x in groupby(c)]
    return len(cons) == 6


color = list(map(int, input().strip().split()))

faces = [[2, 4, 6, 8, 10, 12, 23, 21], [13, 14, 5, 6, 17, 18, 21, 22],
         [15, 16, 7, 8, 19, 20, 23, 24], [1, 3, 5, 7, 9, 11, 24, 22],
         [9, 10, 19, 17, 4, 3, 14, 16], [1, 2, 18, 20, 12, 11, 15, 13]]


def rotate(g, face):
    c = g[:]
    temp1 = c[face[0] - 1]
    temp2 = c[face[1] - 1]
    for i in range(0, 6, 2):
        c[face[i] - 1] = c[face[i + 2] - 1]
        c[face[i + 1] - 1] = c[face[i + 3] - 1]
    c[face[-2] - 1] = temp1
    c[face[-1] - 1] = temp2
    return c


def canSolve(c):
    for i in faces:
        rot = rotate(c, i)
        if isSolved(rot):
            return True
        x = list(reversed(i))
        rot2 = rotate(c, x)
        if isSolved(rot2):
            return True
    return False


if canSolve(color):
    print("YES")
else:
    print("NO")
