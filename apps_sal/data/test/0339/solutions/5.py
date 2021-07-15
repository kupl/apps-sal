n = int(input())
k = int(input())
a = int(input())
b = int(input())
c = 0
while(n>1):
    if(n<k):
        c += a*(n - 1)
        n = 1
    else:
        if(n%k!=0):
            t = n%k
            n -= t
            c += t*a
        else:
            if(b<(n-n//k)*a):
                n = n//k
                c += b
            else:
                c += a*(n - 1)
                n = 1
print(c)

