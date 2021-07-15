##divisor func.
def div(n):
    res=[]
    i=int(1)
    while i*i<=n:
        if n%i==0:
            res.append(i)
            if n!=i**2:
                res.append(n//i)
        i+=1
    res.sort()
    return res

s,p=map(int,input().split())
A=div(p)
for a in A:
    if a+p//a==s:
        print('Yes')
        return
print('No')
