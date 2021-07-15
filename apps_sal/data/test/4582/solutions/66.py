a,b=map(str,input().split())

if a=='H':
    a=1
else:
    a=0
if b=='H':
    b=1
else:
    b=0

if a^b==0:
    print('H')
else :
    print('D')
