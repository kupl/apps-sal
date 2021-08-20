n = int(input())
a = int(input())
b = int(input())
c = int(input())
if n == 1:
    print(0)
else:
    print(min([a * (n - 1), b * (n - 1), c * (n - 2) + a, c * (n - 2) + b]))
