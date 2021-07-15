n=input()
xx=n.split()
y=input()
yy=y.split()
su=0
for i in range(0,int(xx[0])-int(xx[1])):
    su+=int(yy[i])
su+=int(xx[1])*int(xx[2])
print(su)

