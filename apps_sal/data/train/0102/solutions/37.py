t=int(input())
for i in range(t):
    n=int(input())
    a=0;p='1';c=1;u=1
    while True:
        if int(p)<=n:
            a+=1
        else:
            break
        c+=1
        if c==10:
            u+=1
            p='1'*u
            c=1
        else:
            p=str(int('1'*u)*c)
    print(a)    
