n=int(input())
a=list(map(int,input().split()))
sm=sum(a)
s=a.pop(0)
mn=abs(sm-s*2)
for i in a[:-1]:
  s+=i
  mn=min(mn,abs(sm-s*2))
  
print(mn)
