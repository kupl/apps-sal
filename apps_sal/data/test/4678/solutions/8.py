s=int(input())
x=list(map(int,input().split()))
sum=0
maxi=x[0]
for i in x:
  maxi=max(maxi,i)
  sum+=(maxi-i)
print(sum)
