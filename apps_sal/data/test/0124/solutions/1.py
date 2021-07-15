x, y, z= map(int, input().split())
a, b, c = map(int,input().split())
if a >= x:
    a -= x
    s = a + b
    if s >= y:
        s -= y
        s += c
        if s >= z:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
