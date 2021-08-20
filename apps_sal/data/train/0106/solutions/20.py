q = int(input())
while q > 0:
    q = q - 1
    L = []
    n = int(input())
    for i in range(n):
        L.append(tuple(map(int, input().split())))
    d = {}
    ind = 0
    for i in L:
        if i not in d:
            d[i] = []
        d[i].append(ind)
        ind += 1
    S = sorted(L)
    r = S[0][1]
    i = 1
    while i < n:
        if S[i][0] > r:
            break
        r = max(r, S[i][1])
        i += 1
    if i == n:
        print(-1)
    else:
        while i < n:
            d[S[i]].append(-2)
            i += 1
        for i in L:
            if d[i][-1] == -2:
                print(2, end=' ')
            else:
                print(1, end=' ')
        print()
