#54
a,b=list(map(int,input().split()))
if ((a==1 and b!=1) or (a>b and b!=1)):
    print('Alice')
elif ((b==1 and a!=1) or (b>a and a!=1)):
    print('Bob')
else:
    print('Draw')

