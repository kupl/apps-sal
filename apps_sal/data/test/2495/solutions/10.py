A=int(input())
l=list(map(int,input().split()))
sum_n=0
ans=0
caseA=0
for i in range(A):
   sum_n+=l[i]
   if i%2==0:
      if 0<sum_n:
         continue
      else:
         ans+=abs(1-sum_n)
         sum_n=1
   else:
      if sum_n < 0:
         continue
      else:
         ans+=abs(-1-sum_n)
         sum_n=-1
caseA=ans
ans=0
sum_n=0
for i in range(A):
   sum_n+=l[i]
   if i%2==1:
      if 0<sum_n:
         continue
      else:
         ans+=abs(1-sum_n)
         sum_n=1
   else:
      if sum_n < 0:
         continue
      else:
         ans+=abs(-1-sum_n)
         sum_n=-1
print(min(ans,caseA))
