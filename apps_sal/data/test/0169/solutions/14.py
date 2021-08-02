n, a, b, c = int(input()), int(input()), int(input()), int(input())
l = 0
if b - c < a and n >= c:
    l = (n - c) // (b - c)
    n -= l * (b - c)
l += n // a
print(l)
