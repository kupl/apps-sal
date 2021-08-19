q = int(input())


def solve():
    n = int(input())
    p = [int(x) for x in input().split()]
    days = [0] * n
    d = 0
    for i in range(n):
        d = 0
        j = p[i] - 1
        d += 1
        while j != i:
            d += 1
            j = p[j] - 1
        days[i] = str(d)
    print(' '.join(days))


for _ in range(q):
    solve()
