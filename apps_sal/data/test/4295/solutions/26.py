import numpy

n, m = input().split()
n = numpy.int64(n)
m = numpy.int64(m)
n = n % m
print(min(n, m-n))
