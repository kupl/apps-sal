a,b=input().split( )
a=int(a)
b=int(b)
t=a
while a//b>=1:
    t+=a//b
    a=a//b+a%b
print(t)


