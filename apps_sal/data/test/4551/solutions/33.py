a,b,c,d = map(int,input().split())
e,f=a+b,c+d
if e<f:
    print("Right")
elif e==f:
    print("Balanced")
else:
    print("Left")
