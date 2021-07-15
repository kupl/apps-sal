import numpy
a,b,x=list(map(int,input().split()))
V=a*a*b
if x<=V/2:
    y=2*x/b/a
    theta=numpy.arctan(b/y)
    print((theta*360/2/numpy.pi))
else:
    x=V-x
    y=2*x/a/a
    theta=numpy.arctan(y/a)
    print((theta*360/2/numpy.pi))

