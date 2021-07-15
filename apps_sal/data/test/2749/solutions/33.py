h,w,n,*a=map(int,open(0).read().split())
l=[]
for i in range(n): l+=[i+1]*a[i]
for i in range(h): print(*l[i*w:i*w+w][::1-i%2*2])
