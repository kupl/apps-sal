n=int(input())
x_list=[]
u_list=[]
for i in range(n):
  x,u=input().split()
  x_list.append(float(x))
  u_list.append(u)
sum=0
for i in range(n):
  if u_list[i]=="JPY":
    sum+=x_list[i]
  else:
    sum+=x_list[i]*380000.0
print(sum)
