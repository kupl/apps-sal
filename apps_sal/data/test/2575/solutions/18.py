t = int(input())
for i in range(t):
    a = int(input())
    if 360 / (180 - a) == 360 // (180 - a):
        print("YES")
    else:
        print("NO")

