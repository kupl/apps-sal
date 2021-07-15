a,b,c = map(int,input().split())
if a != b and a == c:
    print(b)
elif a != b and a != c:
    print(a)
else:
    print(c)
