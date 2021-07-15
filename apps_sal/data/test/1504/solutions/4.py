from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    #don't

    n,k = map(int,stdin.readline().split() )
    l1,r1 = map(int,stdin.readline().split())
    l2,r2 = map(int,stdin.readline().split())

    #don't
    if l1 >= r2 or l2 >= r1:
        ans = float("inf")
        for usenum in range(1,n+1):

            if max(abs(l1-r2),abs(l2-r1))*usenum >= k:
                ans = min(ans , min(abs(l1-r2),abs(l2-r1))*usenum + k)
            else:
                rem = k - max(abs(l1-r2),abs(l2-r1))*usenum
                ans = min(ans , min(abs(l1-r2),abs(l2-r1))*usenum + max(abs(l1-r2),abs(l2-r1))*usenum + rem*2)
        print (ans)

    else:
        ans = float("inf")
        over = min(r1-l1 , r2-l2 , r1-l2 , r2-l1)
        usenum = n

        if over * usenum >= k:
            print (0)
            continue
        k -= over * usenum
        useable = max(r1-l1 , r2-l2 , r1-l2 , r2-l1) - over

        if useable * usenum >= k:
            print (k)
            continue
        else:
            rem = k - useable * usenum
            print (useable * usenum + rem*2)
