x,y = map(str,input().split())
al = list("ABCDEF")
x = al.index(x)
y = al.index(y)
if x>y:
    print(">")
elif x<y:
    print("<")
else:
    print("=")
