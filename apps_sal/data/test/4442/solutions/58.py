a,b=map(int,input().split())
A=0
B=0
for i in range(a):
    A += b*10**i
for i in range(b):
    B += a*10**i
if a>b:
    print (A)
else:
    print (B)
