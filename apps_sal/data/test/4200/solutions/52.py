from sys import stdin,stdout
for _ in range(1):#int(stdin.readline())):
    # n=int(stdin.readline())
    n,m=list(map(int,stdin.readline().split()))
    a=list(map(int,stdin.readline().split()))
    a.sort(reverse=True)
    sm=sum(a);c=0
    lim=4*m
    lim=(1/lim)*sm
    for i in range(n):
        if a[i]<lim:break
        c+=1
    print('Yes' if c>=m else 'No')
