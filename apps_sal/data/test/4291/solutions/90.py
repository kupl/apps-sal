n,q = list(map(int,input().split()))
s = input()

lr = [list(map(int,input().split())) for i in range(q)]

acm = [0]*(n+1)

for i in range(1,n):
    if(s[i-1]=='A' and s[i]=='C'):
        acm[i] = acm[i-1] + 1 
    else:
        acm[i]=acm[i-1]

acm[n] = acm[n-1] 

for lis in lr:
    l,r =lis
    print((acm[r-1]-acm[l-1]))

