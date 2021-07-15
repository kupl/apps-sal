a,b,c = list(map(int, input().split()))
 
if b - a > 0 and c > 0:
    if (b - a) % c == 0:
        print("YES")
    else:
        print("NO")
elif b - a < 0 and c < 0:
    if (b - a) % c == 0:
        print("YES")
    else:
        print("NO")
elif a - b == 0:
    print("YES")
else:
    print("NO")

