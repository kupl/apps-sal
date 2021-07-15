n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
MAX=1000
cost=n-1
start=a[0]
for h in range(1,MAX,1):
    c=0
    for i,height in enumerate(a):
        c += int(h+i*k != height)
    if c<cost:
        cost=c
        start=h
print(cost)
for i,height in enumerate(a):
    desired_height = start+i*k
    if desired_height != height:
        diff = height - desired_height
        if diff>0:
            print('{0} {1} {2}'.format('-',i+1,abs(diff)))
        else:
            print('{0} {1} {2}'.format('+',i+1,abs(diff)))

