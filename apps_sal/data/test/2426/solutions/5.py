T = int(input())
for cas in range(T):
    n = int(input())
    a = [int(e) for e in input().split()]
    ok = False
    b = []
    for (i, j) in enumerate(a):
        if j % 2 == 0:
            print(1)
            print(i + 1)
            ok = True
            break
        else:
            b.append(i + 1)
        if len(b) >= 2:
            print(2)
            print(b[0], b[1])
            ok = True
            break
    if not ok:
        print(-1)
