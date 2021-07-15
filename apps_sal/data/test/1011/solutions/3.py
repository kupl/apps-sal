

n = int(input())
a = [int(s) for s in input().split()]
m = int(input())
b = [int(s) for s in input().split()]

INF = 3000000000
a.sort()
b.sort()

a.append(INF)
b.append(INF)
i = 0
j = 0

bestd = 0
bestadv = (n-m)*3
besta = 3*n
bestb = 3*m
cura = 3*n
curb = 3*m
while i<n or j<m:
    d = min(a[i],b[j])
    while i<n and a[i]<=d:
        cura-=1
        i+=1
    while j<m and b[j]<=d:
        curb-=1
        j+=1
    
    if cura - curb>bestadv:
        bestadv = cura-curb
        besta = cura
        bestb = curb
##    print(d,i,j,cura,curb,bestadv)

print('{0}:{1}'.format(besta,bestb))

    
        
        


