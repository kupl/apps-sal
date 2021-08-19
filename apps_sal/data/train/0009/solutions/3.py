for _ in range(int(input())):
    s = input()
    ar = []
    cur = 0
    for c in s:
        if c == '1':
            cur += 1
        else:
            ar.append(cur)
            cur = 0
    if cur != 0:
        ar.append(cur)
    ar.sort()
    ar.reverse()
    print(sum(ar[::2]))
