def f(n):
    k=((1+8*n)**0.5-1)/2
    if int(k)==k:k=int(k)
    else:k=int(k)+1
    if n%2:
        if k%4 in [1,2]:return k
        else:
            while k%4 not in [1,2]:k+=1
            return k
    else:
        if k%4 not in [1,2]:return k
        else:return (k//4)*4+3

for i in ' '*int(input()):
    a,b=map(int,input().split())
    print(f(abs(a-b)))
