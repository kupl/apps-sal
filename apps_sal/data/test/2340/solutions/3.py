q=int(input())
for _ in range(q):
    h,n=[int(w) for w in input().split()]
    p=[int(w) for w in input().split()]
    p.append(0)
    r=0
    i=1
    while i<n:
        if p[i]==p[i+1]+1:
            i+=2
        else:
            i+=1
            r+=1
    print(r)

