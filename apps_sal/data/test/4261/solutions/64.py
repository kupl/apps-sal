a,b,c = map(int,input().split())

x = a - b
y = c - x

if y <= 0:
    print("0")

else:
    print(y)
