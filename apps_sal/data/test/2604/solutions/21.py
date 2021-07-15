q,w=list(map(int,input().split()))
e=0
r=q-w
for i in range(0,int(input())):
    a,s,d=list(map(int,input().split()))
    f=(a*a+s*s)**0.5
    if ((f+d<=q)&(f-d>=r)):
        e+=1
print(e)

