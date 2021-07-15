D = {}


def h(m,n,answ,k):
    x = answ
    for i in range(1,(n+2)//2):
        if k >= i*m:
            if m**2+ans(m,n-i,k-i*m) < x:
                x = m**2+ans(m,n-i,k-i*m)
        if k <= (n-i)*m:
            if m**2+ans(m,n-i,k) < x:
                x = m**2+ans(m,n-i,k)
        if k >= (n-i)*m:
            if m**2+ans(m,i,k-(n-i)*m) < x:
                x = m**2+ans(m,i,k-(n-i)*m)
        if k <= i*m:
            if m**2+ans(m,i,k) < x :
                x = m**2+ans(m,i,k)
    return x
def ans(m,n,k):
    if k == 0:
        D[(m,n,k)] = 0
        D[(n,m,k)] = 0
        return 0
    if m*n == k:
        D[(m,n,k)] = 0
        D[(n,m,k)] = 0
        return 0
    elif m == 1:
        D[(m,n,k)] = 1
        D[(n,m,k)] = 1
        return 1
    elif n == 1:
        D[(m,n,k)] = 1
        D[(n,m,k)] = 1
        return 1
    elif (m,n,k) in D:
        return D[(m,n,k)]
    else:
        answ = (n**2)*m
        t = h(m,n,answ,k)
        if t < answ:
            answ = t
        s = h(n,m,answ,k)
        if s < answ:
            answ = s
        D[(m,n,k)] = answ
        D[(n,m,k)] = answ
        return answ

for i in range(30,0,-1):
    for j in range(i,0,-1):
        for k in range(0,min(i*j,50)+1):
            ans(i,j,k)

t = int(input())

for i in range(t):
    m,n,k = [int(x) for x in input().split()]
    print(D[(m,n,k)])
