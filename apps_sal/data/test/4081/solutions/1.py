n = int(input())
a = list(map(int,input().split()))
t = 0
c = 0
l = 0
b = ''
r = n-1
while l<=r:
    m1 = min(a[l],a[r])
    m2 = max(a[l],a[r])
    if m1>t:
        t = m1
        if m1==a[r]:
            r-=1
            b+='R'
        elif m1==a[l]:
            l+=1
            b+='L'
        c+=1
    elif m2>t:
        t = m2
        if m2==a[r]:
            r-=1
            b+='R'
        elif m2==a[l]:
            l+=1
            b+='L'
        c+=1
    else:
        break

print(c)
print(b)

