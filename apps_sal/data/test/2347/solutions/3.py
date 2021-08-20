for _ in range(int(input())):
    p = input().rstrip()
    h = input().rstrip()
    p = sorted(p)
    ok = False
    for i in range(len(h) - len(p) + 1):
        q = sorted(h[i:i + len(p)])
        if p == q:
            ok = True
            break
    print('YES' if ok else 'NO')
