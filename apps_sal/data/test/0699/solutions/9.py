
a = input().split()
y = int(a[0])
k = int(a[1])
n = int(a[2])

xl = []
xf = -1

div = n // k
mul = div * k
xmax = mul - y

if xmax < 1:
    print(-1)
else:
    xl.append(xmax)
    while True:
        xmax -= k
        if xmax < 1:
            break
        xl.append(xmax)

    xl.sort()
    ans = ""
    for k in xl:
        ans += str(k) + " "
    print(ans)
