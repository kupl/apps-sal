a,b = list(map(int,input().split()))
if b-a>=5:
    print(0)
else:
    b = b%10
    a = a%10
    if b<a:
        b+=10
    p = 1
    for i in range(1,b-a+1):
        p *= (a+i)
    print(p%10)


