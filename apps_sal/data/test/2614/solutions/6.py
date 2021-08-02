for i in ' ' * int(input()):
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    pt = 0
    M = []
    ct = 0
    while pt < n - 1:
        pt += 1
        ct += 1
        if L[pt] != L[pt - 1]:
            M.append(ct)
            ct = 0
    ct += 1
    M.append(ct)
    M.sort()
    mx = max(M)
    count = 0
    mxcount = 0
    for i in M:
        if i == mx:
            mxcount += 1
        else:
            count += i
    ans = mxcount + (count // (mx - 1)) - 1
    print(ans)
