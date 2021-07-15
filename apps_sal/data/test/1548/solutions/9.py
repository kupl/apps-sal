n=int(input())
counter=0
a=sorted([int(x) for x in input().split()])
for i in range(n//2):
    counter+=a[i]
s=sum(a)
print((s-counter)**2+counter**2)

