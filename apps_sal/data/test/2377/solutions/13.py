n,h,*L=map(int,open(x:=0).read().split());a=max(L[::2]);b=sorted(L[1::2])
while b and b[-1]>a>0<h:h-=b.pop();x+=1
print(x--h//a*(h>0))
