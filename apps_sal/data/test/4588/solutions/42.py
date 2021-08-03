x, y = list(map(str, input().split()))
if x == y:
    print("=")
elif x < y:
    print("<")
else:
    print(">")
