# a and m must be coprime!
# returns x such that xa = 1 mod m
def modinverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x += m0
    
    return x
# runs in log(m)

M = (10 ** 9) + 7

line = [int(x) for x in input().split()]

n = line[0]
m = line[1]

Mi = modinverse(m, M)
Ti = modinverse(2, M)

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

Pkp1 = 0
Pk = 0

if a[-1] == 0 and b[-1] == 0:
    Pkp1 = ((m-1) % M) * Mi * Ti
elif a[-1] == 0:
    Pkp1 = ((m-b[-1]) % M) * Mi
elif b[-1] == 0:
    Pkp1 = ((a[-1]-1) % M) * Mi
else:
    if a[-1] > b[-1]:
        Pkp1 = 1
    else:
        Pkp1 = 0

Pk = Pkp1

for i in range(1, n):
    j = n - (i + 1)
    
    if a[j] == 0 and b[j] == 0:
        Pk = ((2*Pkp1+m-1) % M) * Mi * Ti
    elif a[j] == 0:
        Pk = ((m-b[j]+Pkp1) % M) * Mi
    elif b[j] == 0:
        Pk = ((Pkp1+a[j]-1) % M) * Mi
    else:
        if a[j] > b[j]:
            Pk = 1
        elif a[j] < b[j]:
            Pk = 0
        else:
            Pk = Pkp1

    Pkp1 = Pk

print(Pk % M)

