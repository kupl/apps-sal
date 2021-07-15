for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    pos,neg = 0,0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
    ans = -10**18
    arr.sort()
    i = 0
    while i<=4 and i<=neg:
        cur = 1
        for j in range(i):
            cur = cur*arr[j]
        j = n-1
        while j>=(n-(5-i)):
            cur = cur*arr[j]
            j-=1
        ans = max(ans,cur)
        i+=2
    print(ans)
