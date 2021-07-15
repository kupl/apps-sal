n=int(input())
l=[int(input()) for i in range(n)]

lis=[i for i in l if i%10!=0]

sum_l=sum(l)

if sum_l%10!=0:
  print(sum_l)
else:
  if len(lis)==0:
    print(0)
  else:
    print(sum_l-min(lis))
