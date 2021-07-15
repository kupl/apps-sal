for _ in range(int(input())):
    n, b = int(input()), list(map(int, input().split()))

    d = {e: True for e in range(1, 2*n + 1)}

    a = [0] * (2 * n)
    for i in range(n):
        a[2*i] = b[i]
        d[b[i]] = False

    ok = True
    for i in range(1, 2*n, 2):
        e = a[i-1] + 1
        while e <= 2*n:
            if d[e]:
                a[i] = e
                d[e] = False
                break
            e += 1

        if e > 2*n:
            ok = False
            break

    if not ok:
        print(-1)
    else:
        print(*a)
