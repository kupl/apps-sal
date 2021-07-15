t = int(input())

for _ in range(t):
    n = int(input())
    l = [[] for _ in range(5001)]
    r = [[] for _ in range(5001)]
    a = [-1 for _ in range(n)]
    for i in range(n):
        l0, r0 = input().split()
        l[int(l0)].append(i)
        r[int(r0)].append(i)

    q = []
    for e, (l, r) in enumerate(zip(l, r)):
        for h in sorted(l):
            q.insert(0, h)
        if q:
            ch = q.pop()
            a[ch] = e
        for h in r:
            if h in q:
                q.remove(h)
                a[h] = 0

    print(*a)

