for _ in range(int(input())):
    n = int(input())
    ar = []
    kek = set()
    for i in range(1, n + 1):
        kek.add(i)
    kek.discard(n - 1)
    ar.append(n - 1)
    for i in range(n):
        if ar[-1] - 3 in kek:
            kek.discard(ar[-1] - 3)
            ar.append(ar[-1] - 3)
        elif ar[-1] - 2 in kek:
            kek.discard(ar[-1] - 2)
            ar.append(ar[-1] - 2)
        elif ar[-1] - 4 in kek:
            kek.discard(ar[-1] - 4)
            ar.append(ar[-1] - 4)
        elif ar[-1] + 3 in kek:
            kek.discard(ar[-1] + 3)
            ar.append(ar[-1] + 3)
        elif ar[-1] + 2 in kek:
            kek.discard(ar[-1] + 2)
            ar.append(ar[-1] + 2)
        elif ar[-1] + 4 in kek:
            kek.discard(ar[-1] + 4)
            ar.append(ar[-1] + 4)
    if n == 2 or n == 3 or n == 1:
        print(-1)
    else:
        print(*ar)
