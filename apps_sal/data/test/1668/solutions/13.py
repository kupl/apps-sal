t = int(input())
for i in range(t):
    n = int(input())
    a = dict()
    b = []
    for i in range(n):
        c = input()
        a[c] = a.get(c, -1) + 1
        b.append(c)
    print(sum(a.values()))
    rlb = list(range(len(b)))
    for i in rlb:
        v = b[i]
        if a.get(v, 0) == 0:
            print(v)
        else:
            v, vo = v[1:], v
            for i in range(10):
                if not str(i) + v in a:
                    a[str(i) + v] = 0
                    a[vo] -= 1
                    print(str(i) + v)
                    break
