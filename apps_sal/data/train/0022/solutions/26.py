t=int(input())
for i in range(t):
    a1,k=map(int,input().split())
    an=a1
    for j in range(1,k):
        astr=str(an)
        min=9
        max=0
        for r in range(len(astr)):
            if int(astr[r])<min:
                min=int(astr[r])
            if int(astr[r])>max:
                max=int(astr[r])
        an+=min*max
        if min==0:
            break
    print(an)
