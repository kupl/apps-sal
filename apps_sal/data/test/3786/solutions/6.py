n=int(input())
a=[0,0]+list(map(int,input().split()))
b=[0]*(n+1);c=[0]*(n+1)
for i in range(2,n+1):
       if a[i]==1:
              b[i]=1
for i in range(2,n+1):
       cou=0;s=i
       while b[s]==0:  
              cou+=1;s=a[s]
       b[i]=cou+b[s]
for i in b[2:]:
       c[i]+=1
ans=1
for i in c:
       ans+=i%2
print(ans)
