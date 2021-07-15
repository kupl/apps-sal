q=int(input())
a=[1, 6, 28, 120, 496, 2016, 8128, 32640, 130816]
s=0
for i in a:
    if q%i==0:
        s=i
print(s)

