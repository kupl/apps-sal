import collections
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def solve(n, a, b):
    c = collections.Counter(b)
    b = sorted(set(b))
    nex = list(range(1,n)) + [0]
    res = []

    for x in a:
        target = (n - x) % n
        while c[target] == 0:
            if c[nex[target]] == 0:
                nex[target] = nex[nex[target]]
            target = nex[target]

        res.append((x+target)%n)
        c[target] -= 1
    return ' '.join(map(str, res))

print(solve(n, a, b))
