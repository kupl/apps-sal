from collections import Counter
n=int(input())
if n<5:
    d={2:1,3:3,4:6}
    print(d[n])
    return
z=len(str(n//5))
nn=5*10**(z-1)
n0=n-nn+1
if n0<nn:
    print(n0)
elif n0==nn:
    print(n0-1)
elif n0<=2*nn:
    print(n0-1)

elif n0<3*nn:
    print(n0*2-2*nn-1)
elif n0==3*nn:
    print(n0*2-2*nn-2)
elif n0<=4*nn:
    print(n0*2-2*nn-2)

elif n0<5*nn:
    print(n0*3-6*nn-2)
elif n0==5*nn:
    print(n0*3-6*nn-3)
elif n0<=6*nn:
    print(n0*3-6*nn-3)

elif n0<7*nn:
    print(n0*4-12*nn-3)
elif n0==8*nn:
    print(n0*4-12*nn-4)
elif n0<=8*nn:
    print(n0*4-12*nn-4)

elif n0<9*nn:
    print(n0*5-20*nn-4)
elif n0==9*nn:
    print(n0*5-20*nn-5)
