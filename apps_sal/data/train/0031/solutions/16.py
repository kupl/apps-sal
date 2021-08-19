def rilist():
    return [int(i) for i in input().split()]


def rlist():
    return [i for i in input().split()]


def rint():
    return int(input())


def rfloat():
    return float(input())


def pmat(mat):
    for i in range(len(mat)):
        a = ' '.join(map(str, mat[i]))
        print(a)
    print()


d = {'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1)}


def solve(t):
    path = input()
    curr = (0, 0)
    tmp = {}
    res = 0
    for p in path:
        (a, b) = d[p]
        next = (curr[0] + a, curr[1] + b)
        key = sorted((curr, next), key=lambda x: x[0])
        key = sorted(key, key=lambda x: x[1])
        key = tuple(key)
        curr = next
        res += tmp.get(key, 5)
        tmp[key] = 1
    print(res)


test = int(input())
for tc in range(test):
    solve(tc + 1)
