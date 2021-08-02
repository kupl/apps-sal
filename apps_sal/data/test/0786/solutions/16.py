n = int(input())
c, div = map(int, input().split())
if (div == 1):
    x = None
    y = 1900
else:
    x = 1899
    y = None
proof = True
for i in range(n - 1):
    if (x != None):
        x += c
    if (y != None):
        y += c
    c, div = map(int, input().split())
    if (div == 1):
        if (x != None) and (x < 1900):
            proof = False
        else:
            if (y == None):
                y = 1900
            else:
                y = max(y, 1900)
    else:
        if (y != None) and (y > 1899):
            proof = False
        else:
            if (x == None):
                x = 1899
            else:
                x = min(x, 1899)
if (proof):
    if (x == None):
        print("Infinity")
    else:
        print(x + c)
else:
    print("Impossible")
