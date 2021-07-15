n,m=list(map(int,input().split()))



#各iはn//m
#+
#if i <=n%m:
#+1

LIST=[None]*(m+1)

for i in range(1,m+1):
    LIST[i]=n//m

    if i<=n%m:
        LIST[i]+=1

ANS=0
for i in range(1,m+1):
    for j in range(1,m+1):
        if (i**2+j**2)%m==0:
            ANS+=LIST[i]*LIST[j]

print(ANS)

