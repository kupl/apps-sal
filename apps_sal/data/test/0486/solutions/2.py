x=int(input())
    
def numDigits(r):
    m=str(r)
    return len(m)
    
def prodDigits(r):
    m=str(r)
    k=1
    for i in range(len(m)):
        k*=int(m[i])
    return k

l=[]
for i in range(numDigits(x)):
    l.append(prodDigits(x))
    l.append(prodDigits(x-(x%(10**i))-1))
print(max(l))
