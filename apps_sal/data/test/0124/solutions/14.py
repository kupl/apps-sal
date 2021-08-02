x, y, z = list(map(int, input().split()))
a, b, c = list(map(int, input().split()))
if a >= x:
    a -= x
    d = min(y, a)
    a -= d
    y -= d
    if (b >= y):
        b -= y
        if a + b + c >= z:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
