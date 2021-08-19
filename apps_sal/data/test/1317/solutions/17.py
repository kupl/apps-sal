(n, m) = [int(w) for w in input().split()]
d = n // m
r = n % m
s = d * d
a = 0
for i in range(1, m + 1):
    for j in range(1, m + 1):
        if (i * i + j * j) % m == 0:
            a += d * d
            if i <= r:
                a += d
            if j <= r:
                a += d
            if i <= r and j <= r:
                a += 1
print(a)
