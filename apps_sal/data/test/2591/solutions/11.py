t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    s = 0
    e = n - 1
    l2 = []
    c = True
    while s <= e:
        if c:
            l2.append(l[s])
            s += 1
        else:
            l2.append(l[e])
            e -= 1
        c = not c
    print(" ".join(map(str, l2[::-1])))

