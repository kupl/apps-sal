a=int(input())
b=[input().split() for i in range(a)]
c=0
for i in range(a):
  if b[i][1]=="JPY":
    c=c+int(b[i][0])
  if b[i][1]=="BTC":
    c=c+float(b[i][0])*380000
print(c)
