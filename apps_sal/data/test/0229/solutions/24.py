n = int(input())
a = list(map(int, input().split()))

b = set(a)

if len(b) >= 4:
    print("NO")
else:
    x = list(b)
    x.sort()
    if len(x) == 1:
        print("YES")
    elif len(x) == 2:
        print("YES")
    else:
        if x[1] * 2 == x[0] + x[2]:
            print("YES")
        else:
            print("NO")

