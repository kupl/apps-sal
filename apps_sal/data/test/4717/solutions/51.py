x,a,b = map(int,input().split())

a = abs(a-x)
b = abs(b-x)

if a < b:
    print("A")
else:
    print("B")
