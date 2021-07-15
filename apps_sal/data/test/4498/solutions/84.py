a,b,c,d=map(int,input().split())

x=abs(b-a)
y=abs(c-b)
z=abs(c-a)


if x<=d and y<=d:
    print('Yes')

elif z<=d:
    print('Yes')

else:
    print('No')
