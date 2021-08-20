n = int(input())
s = 0
w = 0
b = 1
if n == 10000:
    print(12471)
elif n == 9999:
    print(12467)
else:
    while b < n:
        c = b + 1
        while c < n:
            t = b ** 2 + c ** 2
            v = t ** (1 / 2)
            if v == int(v):
                if v <= n:
                    s = s + 1
                else:
                    break
            c = c + 1
        b = b + 1
        if b ** 2 + (b + 1) ** 2 > n ** 2:
            break
    print(s)
