s,p=list(map(int,input().split()))
d=s*s-4*p
p=round(d**0.5)
for i in range(-1,3):
    if (p+i)**2==d:
        print('Yes')
        return
print('No')

