a = int(input())
b=int(a/7)
c=a%7
if c==0:
    print(b*2,b*2)
elif c==1:
    print(b*2,b*2+1)
elif c==6:
    print(b*2+1,b*2+2)
else:
    print(b*2,b*2+2)
