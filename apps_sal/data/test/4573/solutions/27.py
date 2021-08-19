import numpy
N = int(input())
X = [int(x) for x in input().split()]
S = sorted(X)
m0 = numpy.median(S[:-1])
m1 = numpy.median(S[1:])
for x in X:
    if x < m1:
        print(int(m1))
    else:
        print(int(m0))
