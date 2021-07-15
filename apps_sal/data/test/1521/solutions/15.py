a=input().split()
p=int(a[0])
n=int(a[1])
h=[]
flag=1
for i in range(p):
  h.append(0)
for i in range(n):
  work=int(input())
  work=work % p
  if h[work] and flag:
    answer=i+1
    flag=0
  h[work]=1
if flag:
  answer=-1
print(answer)
