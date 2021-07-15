a,b=map(str,input().split())
x = a+b
x = int(x)
y = x**0.5
if y.is_integer():
    print('Yes')
else:
    print('No')
