n, m= map(int, input().split())
got=0
sell={}
buy=0
for i in range(n):
  a,b=map(int,input().split())
  if a not in sell:
    sell[a]=0
  sell[a]+=b
sell=sorted(sell.items())
if m<=sell[0][1]:
  print(m*(sell[0][0]))
  return
for lis in sell:
  got+=lis[1]
  if got>m:
    buy+=(m-got+lis[1])*lis[0]
    print(buy)
    return
  else:
    buy+=(lis[0])*(lis[1])
