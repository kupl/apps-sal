n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
x *= 2
for i in range(n):
    kol = x + y
#    print(x,y,kol,a[i])
    if kol >= a[i]:
        if a[i] % 2 != 0:
            if y > 0:
                y -= 1
                a[i] -= 1
            else:
                x -= 2
                a[i] -= 1
        x -= a[i]
        if x < 0:
            y += x
            x = 0
#        print(x,y,kol,a[i])
    else:
        print(i)
        break
else:
    print(i + 1)
