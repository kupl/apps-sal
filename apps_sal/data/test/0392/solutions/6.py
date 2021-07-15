def fct(n):
    r = []
    for i in range(1,int(n**.5)+1):
        if n%i == 0:
            r.append(i)
            r.append(int(n/i))
    return r

def lov(n):
    i = 2
    f = 0
    while i**2<=n:
        if n%i**2 == 0:
            
            f = 1
            break
        i += 1
    return f

n = int(input())

a = fct(n)
a = sorted(a,reverse=True)
res = 0
for i in a:
    if lov(i) == 0:
        res = i
        break
        
print (res)

