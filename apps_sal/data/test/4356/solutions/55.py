import numpy

n,m = map(int,input().split())
a = numpy.zeros([n,n], dtype=int)
b = numpy.zeros([m,m], dtype=int)
for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == "#":
            a[i,j] = 1
for i in range(m):
    s = input()
    for j in range(m):
        if s[j] == "#":
            b[i,j] = 1

for i in range(n-m+1):
    for j in range(n-m+1):
        if numpy.all(a[i:i+m, j:j+m] == b):
            print("Yes")
            return
print("No")
