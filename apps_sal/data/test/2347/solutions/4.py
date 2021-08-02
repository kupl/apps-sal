for _ in range(int(input())):
    p = sorted(input())
    h = input()

    ok = False

    i = 0
    while i < len(h):
        j = len(h) - 1
        while j >= 0:
            if sorted(h[i:j + 1]) == p:
                ok = True
            j -= 1
        i += 1

    if ok:
        print('YES')
    else:
        print('NO')
