n=int(input())
n+=1
p=[True]*n
pr=[1]*n
m=1
for k in range(2,n):
    if p[k]:
        for i in range(k,n,k):
            p[i]=False
            pr[i]=m
        m+=1
print(' '.join(map(str,pr[2:])))            

