from bisect import bisect_right
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[i-j for i,j in zip(a,b)]
x.sort()
ans=0
for i in x:
  if i>0:ans-=1
  ans+=n-bisect_right(x,-i)
print(ans//2)
