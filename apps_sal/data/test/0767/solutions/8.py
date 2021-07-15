n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
k=n//2
s=0
mas=[0]*n
for i in range(n):
     if mas[i]==1:
          continue
     for j in range(k,n):
          if a[j]-a[i]>=m and mas[j]!=1:
               mas[i]=1
               mas[j]=1
               k=j+1
               s+=1
               break
          if j==n-1:
               print(s)
               return
print(s)
