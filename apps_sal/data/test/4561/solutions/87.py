x,a,b=map(int,input().split())
b -= a
if b <= 0:
    print('delicious')
    
else:
    if b > x:
        print('dangerous')
    else:
        print('safe')
