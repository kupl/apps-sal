n=int(input())
if n%7==0:
    print((n//7)*2,(n//7)*2)
elif n%7==1:
    print((n//7)*2,(n//7)*2+1)
elif n%7==6:
    print((n//7)*2+1,(n//7)*2+2)
else:
    print((n//7)*2,(n//7)*2+2)
