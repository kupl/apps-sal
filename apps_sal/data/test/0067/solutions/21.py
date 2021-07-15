x,y,z=map(int,input().split())
r=x-y
if r<0 and r+z<0:
    print('-')
elif r>0 and r-z>0:
    print('+')
elif r==0 and r+z==0:
    print('0')
else:
    print('?')
