import collections


def solve(n, a, b):
    c = collections.Counter(b)
    nex = list(range(1, n)) + [0]

    res = []
    for x in a:
        v = (n - x) % n
        while c[v] == 0:
            if c[nex[v]] == 0:
                nex[v] = nex[nex[v]]
            v = nex[v]
        c[v] -= 1
        res.append((x + v) % n)
    return ' '.join(map(str, res))


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
