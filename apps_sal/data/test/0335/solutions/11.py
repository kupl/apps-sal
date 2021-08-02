n = int(input())
a = 1
b = 1
c = n - a - b
if c % 3 == 0:
    c -= 1
    b += 1
print(a, b, c)
