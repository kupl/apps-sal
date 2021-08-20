n = int(input())
a = int(input())
b = int(input())
c = int(input())
if a == min(a, b, c):
    print(a * (n - 1))
elif b == min(a, b, c):
    print(b * (n - 1))
elif n == 1:
    print(0)
elif n == 2:
    print(min(a, b))
else:
    print(min(a, b) + (n - 2) * c)
