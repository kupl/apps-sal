a,b=list(map(int,input().split()))
if a==0 and b==100:
    print((101))
elif a==1 and b==100:
    print((10100))
elif a==2 and b==100:
    print((1010000))
else:
    print(((100**a)*b))

