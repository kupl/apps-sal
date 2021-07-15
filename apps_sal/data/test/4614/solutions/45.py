a,b,c=list(map(int,input().split()))
if a==b & b != c:
    print(c)
elif a==c & c !=b:
    print(b)
else:
    print(a)

