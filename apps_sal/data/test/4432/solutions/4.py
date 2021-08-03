for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    i = 1
    b, tmp = [], [a[0]]
    while i < n:
        if a[i] * tmp[0] > 0:
            tmp.append(a[i])
        else:
            b.append(tmp)
            tmp = [a[i]]
        i += 1

    b.append(tmp)

    s = 0
    for bb in b:
        s += max(bb)

    print(s)
