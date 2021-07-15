from bisect import bisect_left,bisect

n=int(input())
l=list(map(int,input().split()))
l.sort()

#n=7
#l=[218, 233, 389, 645, 704, 728, 786]

#print(l)
icnt=0
for a in range(n-2):
    for b in range(a+1,n-1):
        nc=bisect(l,l[a]+l[b]-1)
        if nc>b+1:
            icnt+=nc-(b+1)
#            print(a,b,nc,l[a],l[b],l[a]+l[b])
        
print(icnt)

