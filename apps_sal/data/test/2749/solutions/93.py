h,w,_,*a=map(int,open(0).read().split())
l=[]
for i,c in enumerate(a): l+=[i+1]*c
for i in range(h): print(*l[i*w:-~i*w][::2*(i%2)-1])
