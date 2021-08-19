q = int(input())
b = []
for m in range(q):
    n, k = list(map(int, input().split()))
    l = input()
    k1 = 'R'
    k2 = 'G'
    k3 = 'B'
    for i in range(1, k):
        if k1[i - 1] == 'R':
            k1 = k1 + 'G'
        if k1[i - 1] == 'G':
            k1 = k1 + 'B'
        if k1[i - 1] == 'B':
            k1 = k1 + 'R'
        if k2[i - 1] == 'R':
            k2 = k2 + 'G'
        if k2[i - 1] == 'G':
            k2 = k2 + 'B'
        if k2[i - 1] == 'B':
            k2 = k2 + 'R'
        if k3[i - 1] == 'R':
            k3 = k3 + 'G'
        if k3[i - 1] == 'G':
            k3 = k3 + 'B'
        if k3[i - 1] == 'B':
            k3 = k3 + 'R'
    minn = n
    # print(k1)
    # print(k2)
    # print(k3)
    for i in range(n - k + 1):
        tec = 0
        for j in range(k):
            if l[i + j] != k1[j]:
                tec += 1
        if tec < minn:
            minn = tec
    for i in range(n - k + 1):
        tec = 0
        for j in range(k):
            if l[i + j] != k2[j]:
                tec += 1
        if tec < minn:
            minn = tec
    for i in range(n - k + 1):
        tec = 0
        for j in range(k):
            if l[i + j] != k3[j]:
                tec += 1
                #print(l[i+j], k3[j])
        if tec < minn:
            minn = tec
    b.append(minn)
for i in range(q):
    print(b[i])
