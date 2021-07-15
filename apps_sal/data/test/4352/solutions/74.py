a,b=map(int,input().split())
a=(a-2)%13
b=(b-2)%13
if a<b:print('Bob')
elif a>b:print('Alice')
else:print('Draw')
