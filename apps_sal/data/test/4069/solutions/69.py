x,k,d = list(map(int,input().split()))

ax = abs(x)

kd = k*d

if(ax>kd):
    print((ax-kd))
else:
    num = ax//d
    if((num%2)==(k%2)):
        print((ax-(d*num)))
    else:
        if(num==k):
            print((ax-d*num))
        else:
            print((abs(ax-d*num-d)))

    

