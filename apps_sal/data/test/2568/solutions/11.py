for _ in range(int(input())):
    ar = list(input())
    kek = 0
    lol = 0
    for i in range(len(ar)):
        if ar[i] == '-':
            kek += 1
        else:
            kek -= 1
        if kek > lol:
            lol = kek
    fifi = [-1] * lol
    cur = 0
    for i in range(len(ar)):
        if ar[i] == '-':
            cur += 1
            if cur > 0 and fifi[cur - 1] == -1:
                fifi[cur - 1] = i + 1
        else:
            cur -= 1
    ans = 0
    for elem in fifi:
        ans += elem
    print(len(ar) + ans)

