n=int(input())
alist=list(map(int, input().split()))
blist=list(map(int, input().split()))
clist=list(map(int, input().split()))
alist.sort()
blist.sort()
clist.sort()
import bisect
ans=0
for b in blist:
  num1=n-bisect.bisect(clist,b)
  num2=bisect.bisect_left(alist,b)
  ans+=num1*num2
print(ans)
