n = int(input())
a = 2
b = 1
for i in range(n-1):
    c=b+a
    a,b=b,c
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    print(c)
