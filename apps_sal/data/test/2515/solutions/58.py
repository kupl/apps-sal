q=int(input())
query=[list(map(int,input().split())) for _ in range(q)]
def factorize(n):
    if n==0:
        return 0
    a=[]
    while n%2==0:
        a.append(2)
        n//=2
    f=3
    while f*f<=n:
        if n%f==0:
            a.append(f)
            n//=f
        else:
            f+=2
    if n!=1:
        a.append(n)
    return len(a)
s=[0]*100001 #s[i]==1:iが素数
for i in range(100001):
    s[i]=factorize(i)
j=[0]*100001
count=0
for i in range(100000):
    if s[i]==1:
        if s[(i+1)//2]==1:
            count+=1
            j[i]=count
        else:
            j[i]=count
    else:
        j[i]=count
for l,r in query:
    print(j[r]-j[l-1])
