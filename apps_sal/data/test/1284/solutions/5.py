n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n//2):
  ans+=a[2*i]
ans+=a[n-1]
pointer=n-1
pointer2=0
maxans=ans
for i in range(n):
  ans-=a[pointer2]
  pointer2=(pointer2+2)%n
  ans+=a[(pointer+2)%n]
  pointer=(pointer+2)%n
  maxans=max(ans,maxans)
print(maxans)
