__author__ = 'Rajan'

x=0
y=0
z=0
a1,b1,c1 = map(int,input().split())
x = b1+c1
a2,b2,c2 = map(int,input().split())
y = a2+c2
a3,b3,c3 = map(int,input().split())
z = a3+b3

sum = (x+y+z)//2

a1 = sum-x
b2 = sum-y
c3 = sum-z

print(a1,b1,c1)
print(a2,b2,c2)
print(a3,b3,c3)
