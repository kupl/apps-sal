s, p = list(map(int, input().split()))
n1 = (s+((-s)**2-4*p)**.5)/2
n2 = (s-((-s)**2-4*p)**.5)/2
n1 = int(n1)
n2 = int(n2)
m1 = s-n1
m2 = s-n2
if n1+m1 == s and n1*m1 == p:
    print('Yes')
elif n2+m2 == s and n2*m2 == p:
    print('Yes')
else:
    print('No')

