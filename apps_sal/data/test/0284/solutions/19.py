n = int(input())

x = 1234567
y = 123456
z = 1234

if n < z:
    print("NO")
    return
else:
    a = 0
    while (a * x) <= n:
        b = 0
        while (b * y) + (a * x) <= n:
            if ((n - (b * y + a * x)) % z) == 0:
                print("YES")
                return
            b += 1
        a += 1

print("NO")
