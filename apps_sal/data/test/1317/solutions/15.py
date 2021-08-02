n, m = list(map(int, input().split()))
x = n % m
y = n // m
s = 0
for i in range(1, m + 1):
    for j in range(i, m + 1):
        if (i ** 2 + j ** 2) % m == 0:
            a, b = 0, 0
            if i <= x:
                a = 1
            if j <= x:
                b = 1
            r = (y + a) * (y + b)
            if i != j:
                s += r * 2
            else:
                s += r
print(s)
