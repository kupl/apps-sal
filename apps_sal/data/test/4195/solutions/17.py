D,N = map(int,input().split())
if D==0 and N<=99:
    print(1+N-1)
elif D==0 and N==100:
    print(101)
elif D==1 and N<=99:
    print(100*N)
elif D==1 and N==100:
    print(10100)
elif D==2 and N<=99:
    print(10000*N)
elif D==2 and N==100:
    print(10000*101)
