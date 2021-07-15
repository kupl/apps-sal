s=input()
l,r,u,d=s.count('l'),s.count('r'),s.count('u'),s.count('d'),
x,y=s.count('L')-s.count('R'),s.count('U')-s.count('D'),
r=abs(x)//2+abs(y)//2
if abs(x)%2==abs(y)%2==0:
    print(r)
elif abs(x)%2==abs(y)%2==1:
    print(r+1)
else:
    print('-1')
