n = int(input())
t = 0
for i in range(n):
    a, b = input().split()
    if t == 0 and b != "South":
        print("NO")
        break
    if t == 20000 and b != "North":
        print("NO")
        break
    if b == "North":
        t-=int(a)
        if t<0:
            print("NO")
            break
    if b == "South":
        t+=int(a)
        if t > 20000:
            print("NO")
            break
else:
    if t == 0:
        print("YES")
    else:
        print("NO")
