t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = set()
    d = {}
    for a in l:
        j = 0
        while (a % 2) == 0:
            a = a // 2
            j += 1
        s.add(a)
        if a in d:
            if d[a] < j:
                d[a] = j
        else:
            d[a] = j
    p = 0
    for q in d:
        p += d[q]
    print(p)

