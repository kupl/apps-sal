x, y = map(str, input().split())
#print(int(ord(x)), int(ord(y)))
if x < y:
    print("<")
elif x == y:
    print("=")
else:
    print(">")
