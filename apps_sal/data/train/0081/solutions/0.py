for _ in range(int(input())):
    a, b, c = input(), input(), input()
    n = len(a)

    ok = True
    for i in range(n):
        if c[i] not in [a[i], b[i]]:
            ok = False

    print('YES' if ok else 'NO')
