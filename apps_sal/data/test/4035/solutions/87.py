from decimal import Decimal
a,b=map(int,input().split())

x=[]

s=a/(Decimal('0.08'))
t=(a+1)/(Decimal('0.08'))
u=b/(Decimal('0.1'))
v=(b+1)/(Decimal('0.1'))

x.append(s)
x.append(t)
x.append(u)
x.append(v)

ans=[]

for i in range(int(min(x)),int(max(x))+1):
    if a/(Decimal('0.08'))<=i<(a+1)/(Decimal('0.08')) and b/(Decimal('0.1'))<=i<(b+1)/(Decimal('0.1')):
        ans.append(i)

if not ans:
    print('-1')
else:
    print(min(ans))
