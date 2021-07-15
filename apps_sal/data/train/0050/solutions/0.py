for tcase in range(int(input())):
    n=int(input())
    ls = list(map(int, input().split()))
    oneneed = 2*(n - ls.count(1))
    ldct = {0:0}
    ctr = 0
    eaten = 0
    for i in range(n-1,-1,-1):
        eaten += 1
        ctr += (1 if ls[i] == 2 else -1)
        if ctr not in ldct:
            ldct[ctr] = eaten

    rdct = {0:0}
    ctr = 0
    eaten = 0
    for i in range(n,2*n):
        eaten += 1
        ctr += (1 if ls[i] == 2 else -1)
        if ctr not in rdct:
            rdct[ctr] = eaten
    #print(oneneed, ldct, rdct)

    best=99**99
    for k in list(rdct.keys()):
        otk = oneneed - k
        if otk in ldct:
            best = min(best, rdct[k]+ldct[otk])
    print(best)

