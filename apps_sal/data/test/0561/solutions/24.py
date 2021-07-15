n=int(input())
a=list(map(int,input().split()))
a.sort()
cnt=0
if n==1:
	print(-1)
	return
if n==2:
	if((a[1]-a[0])%2==0 and a[1]!=a[0]):
		print(3)
		print(2*a[0]-a[1],(a[0]+a[1])//2,2*a[1]-a[0])
		return
d=sorted([a[i]-a[i-1] for i in range(1, n)])
if len(set(d))==1:
    if d[0]!=0:
        print(2)
        print(a[0]-d[0], a[-1]+d[0])
    else:
        print(1)
        print(a[0])
    return
if len(set(d)) > 2 or d[-1]!=2*d[-2]:
    print(0)
else:
    print(1)
    for i in range(1, n):
        if a[i]-a[i-1] != d[0]:
            print(a[i-1]+d[0])
