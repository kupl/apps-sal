_,A=open(0);m=x=0
for a in map(int,A.split()):x+=max(m-a,0);m=max(m,a)
print(x)
