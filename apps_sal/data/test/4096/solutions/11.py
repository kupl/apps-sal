n, m=(int(i) for i in input().split())
L=[int(i) for i in input().split()]
p=0
t=1
L.sort()
for i in L:
   p+=i
if p<m:
    print(-1)
    t=0
else:
    for i in range(n):
        s=0
        for j in range(n//(i+1)):
            s+=j
            g=j
        s=s*(i+1)+(g+1)*(n%(i+1))
        if s+m<=p:
            mm=i+1
            break
for u in range(len(L)):
    L=L[1:]
    n=n-1
    p=0
    #print(L)
    for i in L:
        p+=i
    if p>=m:
        for i in range(n):
            s=0
            for j in range(n//(i+1)):
                s+=j
                g=j
            s=s*(i+1)+(g+1)*(n%(i+1))
            if s+m<=p:
                if i+1<mm:
                    mm=i+1
                break
if t:
    print(mm)


        
    

