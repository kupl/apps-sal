import sys
input = sys.stdin.readline
q = int(input())


def find(x):
    while Group[x] != x:
        x = Group[x]
    return x


def Union(x, y):
    if find(x) != find(y):
        Group[find(y)] = Group[find(x)] = min(find(y), find(x))


for testcases in range(q):
    n = int(input())
    P = list(map(int, input().split()))
    Group = [i for i in range(n)]
    for i in range(n):
        Union(i, P[i] - 1)
    G = [find(i) for i in range(n)]
    count = [0] * n
    for g in G:
        count[g] += 1
    for i in range(n):
        print(count[G[i]], end=' ')
    print()
