l=input().split()
n=int(l[0])
m=int(l[1])
l=input().split()
x=int(l[0])
k=int(l[1])
y=int(l[2])
a=input().split()
ai=[int(i) for i in a]
b=input().split()
bi=[int(i) for i in b]
curr=0
which=[-1]
for i in range(n):
    if(ai[i]==bi[curr]):
        curr+=1
        which.append(i)
        if(curr==m):
            break
which.append(n)
ans=0
if(curr!=m):
    print(-1)
else:
    poss=1
    for i in range(1,m+2):
        if(which[i-1]+1==which[i]):
            continue
        if(i==1):
            z=ai[which[i]]
        elif(i==m+1):
            z=ai[which[i-1]]
        else:
            z=max(ai[which[i]],ai[which[i-1]])
        maxa=max(ai[which[i-1]+1:which[i]])
        num=which[i]-which[i-1]-1
        if(maxa>z and num<k):
            poss=0
            break
        if(y*k<=x):
            if(maxa>z):
                ans+=x
                ans+=(num-k)*y
            else:
                ans+=num*y
        else:
            ans+=((num//k)*x)
            ans+=((num%k)*y)
    if(poss==0):
        print(-1)
    else:
        print(ans)
