import math 
m = int(1e6 + 3)
a,b = input().split()
a = int(a)
b = int(b)
A = 1
B = 1
for i in range(2,a + b + 1):
    A=(A*i)%m
    if i<=a:
        B=(B*i)%m
    if i<=b:
        B=(B*i)%m
print((A*pow(B,m-2,m)-1)%m)
