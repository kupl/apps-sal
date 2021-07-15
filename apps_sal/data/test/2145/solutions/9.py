t = int(input())
for i in range (t):
    a, b = list(map(int,input().split()))
    if a > 3:
        print("YES")
    elif a == 1:
        if b == 1:
            print("YES")
        else:
            print("NO")
    else:
        if b < 4:
            print("YES")
        else:
            print("NO")
