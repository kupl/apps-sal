import decimal
decimal.getcontext().prec = 20


def nearest(a):
    a=int(a)
    x=str(decimal.Decimal(a).sqrt()) + '.'
    x=int(x[:x.find('.')])
    return min((a-x*x),(x+1)**2-a)

n=int(input())
b=list(map(int,input().split()))
b.sort()
a=list(map(nearest,b))
a.sort()
if(a[n//2]==0):
    count=0
    for i in range(n//2):
        if(a[i+n//2]==0):
            count+=1
        else:
            break
    for i in range(n//2):
        if(b[i+n//2]==0):
            count+=1
        else:
            break
    print(count)
else:
    print(sum(a[:n//2]))
    

