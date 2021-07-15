N,A,B=list(map(int, input().split()))
s=0
for i in range(1,N+1):
    k=0
    j=i
    while(j>0):
        k+=j%10
        j=j//10
    if (A<=k and k<=B):
        s=s+i
print(s)

