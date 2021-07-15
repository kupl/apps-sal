n,t=map(int, input().split())
c_list,t_list=[],[]
for i in range(n):
  x,y=map(int, input().split())
  c_list.append(x)
  t_list.append(y)
cost=1001
for i in range(n):
  if t_list[i]<=t and c_list[i]<cost:
    cost=c_list[i]
print(cost if cost<1001 else "TLE")
