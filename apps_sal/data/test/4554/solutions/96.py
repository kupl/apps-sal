w,a,b=map(int,input().split())
if ((a<=b and b<=a+w) or (a<=b+w and b<=a)):
    print(0)
elif a+w<b:
    print(b-a-w)
else:
    print(a-b-w)
