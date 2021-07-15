x,a,b=map(int,input().split())
if a>=b:
    print("delicious")
elif 0<b-a<=x:
    print("safe")
else:
    print("dangerous")
