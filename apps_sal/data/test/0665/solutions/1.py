t = int(input())
for i in range(t):
    (n, s) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    (mx, sm, mxi) = (0, 0, 0)
    k = True
    for ii in range(len(a)):
        i = a[ii]
        sm += i
        if i > mx:
            (mx, mxi) = (i, ii)
        if sm > s:
            break
    else:
        k = False
    if k == False:
        print(0)
    else:
        sm -= mx
        ad = 0
        for ij in range(ii, len(a)):
            j = a[ij]
            ad += 1
            sm += i
            if sm > s:
                break
        if ad == 0:
            print(0)
        else:
            print(mxi + 1)
