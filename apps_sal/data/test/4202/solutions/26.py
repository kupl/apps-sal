L,R = map(int,input().split())
if (R//2019 - L//2019) > 0 :
    print(0)
else :
    buf = 2020
    for i in range(L,R+1) :
        for j in range(i+1,R+1) :
            buf = min(buf,((i%2019)*(j%2019))%2019)
    print(buf)
