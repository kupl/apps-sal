def pick(D, v):
    return D[v[0]][v[1]]


def getNeighbours(A, x, y, t='.'):
    neighbours = []
    if x > 0 and A[x - 1][y] == t:
        neighbours.append((x - 1, y))
    if y > 0 and A[x][y - 1] == t:
        neighbours.append((x, y - 1))
    if x < len(A) - 1 and A[x + 1][y] == t:
        neighbours.append((x + 1, y))
    if y < len(A[0]) - 1 and A[x][y + 1] == t:
        neighbours.append((x, y + 1))
    return neighbours


def countNeighbours(A, x, y, t='.'):
    return len(getNeighbours(A, x, y, t))


def hasPath(A, xs, ys, xe, ye):
    A[xe][ye] = '.'
    D = [[-1 for _ in range(len(A[0]))] for _ in range(len(A))]
    D[xs][ys] = 0
    Q = [(xs, ys)]
    while len(Q) > 0:
        u = Q.pop()
        for v in getNeighbours(A, *u):
            if pick(D, v) == -1:
                Q.insert(0, v)
                D[v[0]][v[1]] = pick(D, u) + 1
    return D[xe][ye] != -1


def solve(A, r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        if countNeighbours(A, r1, c1) > 0:
            return True
        else:
            return False
    elif (r2, c2) in getNeighbours(A, r1, c1) or (r2, c2) in getNeighbours(A, r1, c1, 'X'):
        if A[r2][c2] == 'X':
            return True
        elif countNeighbours(A, r2, c2) > 0:
            return True
        else:
            return False
    elif A[r2][c2] == '.':
        if countNeighbours(A, r2, c2) >= 2 and hasPath(A, r1, c1, r2, c2):
            return True
        else:
            return False
    elif A[r2][c2] == 'X':
        if countNeighbours(A, r2, c2) > 0 and hasPath(A, r1, c1, r2, c2):
            return True
        else:
            return False


def main():
    (n, m) = list(map(int, input().split()))
    A = [list(input()) for _ in range(n)]
    (r1, c1) = [int(w) - 1 for w in input().split()]
    (r2, c2) = [int(w) - 1 for w in input().split()]
    ans = solve(A, r1, c1, r2, c2)
    print('YES' if ans else 'NO')


main()
