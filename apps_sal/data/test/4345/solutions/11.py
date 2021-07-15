MAX = 1+2*10**5
MIN = -1

ASC = 0
DSC = 1

n = int(input())
a = list(map(int, input().split()))

asc = MIN
dsc = MAX
res = []

for i in range(n):

    if a[i] > asc and a[i] < dsc:
        # can place in either
        if i+1 == n:
            res.append(DSC)
        elif a[i] > a[i+1]:
            # place in dsc
            res.append(DSC)
            dsc = a[i]
        else:
            # place in asc
            res.append(ASC)
            asc = a[i]  

    elif a[i] > asc:
        # can only place in asc
        res.append(ASC)
        asc = a[i]

    elif a[i] < dsc:
        # can only place in dsc
        res.append(DSC)
        dsc = a[i]

    else:
        # can't place anywhere
        print("NO")
        return
    
print("YES")
print(*res)
