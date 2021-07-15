line=input().split()
n=int(line[0])
w=int(line[1])

minsum=0
a=input().split()
for i in range (n):
    a[i]=int(a[i])
    minsum+=(a[i]+1)//2
if (minsum>w):
    print ("-1")
else:
    vols=[str((a[i]+1)//2) for i in range(n)]
    extra=w-minsum
    while (extra>0):
        maxcup=-1
        maxsize=0
        for i in range (n):
            if a[i]>maxsize:
                maxcup=i
                maxsize=a[i]
        if maxcup==-1:
            print(1+" ")
        vols[maxcup]=str(min(maxsize, (maxsize+1)//2 + extra))
        extra -= int(vols[maxcup])-(maxsize+1)//2
        a[maxcup]=-1
    print(" ".join(vols))

