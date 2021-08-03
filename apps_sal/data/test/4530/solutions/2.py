t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    for i in l:
        d[i] = 0
    for i in l:
        d[i] += 1
    myk = len(d)
    maksik = 0
    dupa = -12131
    for i in l:
        if d[i] > maksik:
            maksik = min(d[i], myk - 1)
        if d[i] > myk:
            dupa = myk
    print(max(maksik, dupa))
