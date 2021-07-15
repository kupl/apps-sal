a,b,c,d=map(int,input().split())
if b<=c or d<=a:
    print('0')
elif b<=d:
    print(min(b-c,b-a))
else:
    print(min(d-a,d-c))
