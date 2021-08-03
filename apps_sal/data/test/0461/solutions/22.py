n = int(input())
a = int(input())
b = int(input())
c = int(input())
if n == 1:
    print(0)
elif c == min(a, b, c):
    print(min(a, b) + (n - 2) * c)
else:
    print((n - 1) * min(a, b))
