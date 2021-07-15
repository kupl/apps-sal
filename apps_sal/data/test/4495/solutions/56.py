a,b,x = list(map(int,input().split()))

if  a%x == 0 :
    print((b//x - a//x + 1))
elif a%x is not 0 :
    print((b//x - a//x))




