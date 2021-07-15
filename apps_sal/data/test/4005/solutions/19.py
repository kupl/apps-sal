a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
flag = 0

if b[0] <= a[0] and b[1] <= a[1] and a[2] <= b[2] and a[3] <= b[3]:
    flag = 1
elif c[0] <= a[0] and c[1] <= a[1] and a[2] <= c[2] and a[3] <= c[3]:
    flag = 1
else:
    if b[0] <= a[0] and b[1] <= a[1]:
        if a[2] <= c[2] and a[3] <= c[3]:
            if a[3] <= b[3] and c[1] <= a[1] and c[0] <= b[2]:
                flag = 1
            elif a[2] <= b[2] and c[0] <= a[0] and c[1] <= b[3]:
                flag = 1
    elif c[0] <= a[0] and c[1] <= a[1]:
        if a[2] <= b[2] and a[3] <= b[3]:
            if a[3] <= c[3] and b[1] <= a[1] and b[0] <= c[2]:
                flag = 1
            elif a[2] <= c[2] and b[0] <= a[0] and b[1] <= c[3]:
                flag = 1

print("YES" if (flag == 0) else "NO")
