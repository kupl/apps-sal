n,m=list(map(int,input().split()))
def parc(pt,j):
    if l[pt[0]][pt[1]]:
        l[pt[0]][pt[1]]=False
        parc(j(pt),j)
def f():
    mv=[lambda x:(x[0]+1,x[1]),lambda x:(x[0]-1,x[1]),lambda x:(x[0],x[1]-1),lambda x:(x[0],x[1]+1)]
    for k in range(2,n):
        for i in range(2,m):
            if l[k][i] and min(l[j[0]][j[1]] for j in [h((k,i)) for h in mv]):
                for j in mv:
                    parc(j((k,i)),j)
                l[k][i]=False
                if max(list(map(max,l))):
                    return False
                return True
    return False

l=[[False]*(m+2)]
for k in range(n):
    l.append([False]+[i=='*' for i in input()]+[False])
l.append([False]*(m+2))
if f():
    print("YES")
else:
    print("NO")

