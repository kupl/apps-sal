n=int(input())
a=list(map(int,input().split()))
s=0
a.sort(reverse=True)
for i in range (n):
    s+=a[i]
cel=int(s/n)
ost=s%n
i=0
kol=0
while a[i]>cel:
    if ost!=0:
        kol+=a[i]-cel-1
        ost-=1
    else:
        kol+=a[i]-cel
    i+=1
print(kol)

