def nod(a,b):
    while a!=0 and b!=0:
        if a>b:
            a,b=b,a%b
        else:
            b,a=a,b%a
    return a+b
n ,k = map(int, input().split())  
a = [int(j) for j in input().split()] 
c = a[0]
for i in range(1,n):
    c = nod(c,a[i])
    if c==1:
        break
e = nod(c,k)
if c==1 or e==1:
    print(k)
    for i in range(k):
        print(i, end=" ")

if e>1:
    c = k//e
    print(c)
    for i in range(c):
        print(i*e, end=' ')
    
    
    

