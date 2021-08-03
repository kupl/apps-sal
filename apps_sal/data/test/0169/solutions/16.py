n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = 0
e = -1
if n >= b:
    d = (n - b) // (b - c)
    e = ((n - b) % (b - c) + c) // a
print(max(d + e + 1, n // a, 0))
