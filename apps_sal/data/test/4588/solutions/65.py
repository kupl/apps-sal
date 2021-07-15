x,y = map(str,input().split())
if ord(x) > ord(y):
    print(">")
elif x == y:
    print("=")
else:
    print("<")
