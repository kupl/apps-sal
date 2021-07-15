n,k=map(int,input().split())
count=0
ba=[0]*(10**5+1)
for i in range(n):
    a,b=map(int,input().split())
    ba[a]+=b
 
for i in range(len(ba)):
    k-=ba[i]
    if k<=0:
        print(i)
        break
