n=int(input())
a=list(map(int,input().split()))
hasil=0
a=sorted(a)
for x in range(n-2):
    for y in range(x+1,n-1):
        for z in range(y+1,n):
            if a[x]!=a[y] and a[y]!=a[z] and a[z]!=a[x]:
                if a[x]+a[y]>a[z]:
                    hasil=hasil+1
print(hasil)
