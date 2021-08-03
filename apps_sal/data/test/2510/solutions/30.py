import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
root = [-1] * N


def find(x):
    if root[x] < 0:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    root[x] += root[y]
    root[y] = x


def size(x):
    x = find(x)
    return -root[x]


for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    union(A, B)

ans = max(map(size, range(N)))
print(ans)
