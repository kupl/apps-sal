n=input()
x,y=n.split()
y=int(y)
su=0
for i in range(1,int(x)+1):
    z=int(str(i)+str(i)[::-1])
    su+=z
    su%=y
print(su)

