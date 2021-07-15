
a,b=map(int,input().split())
if b>=a:
    print('0')
elif a-2*b >= 0:
    print(a-2*b)
else:
    print('0')
