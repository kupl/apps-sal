n = int(input())
a, t = n - 1, 1
n -= 1
i = 2
while i <= n:
    a += n // i * t
    i *= 2
    t *= 2
print(a)

