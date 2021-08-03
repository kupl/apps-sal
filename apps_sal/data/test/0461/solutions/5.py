n = int(input())
a = int(input())
b = int(input())
c = int(input())
x = 0
if n > 1:
    x = min(a, b)
    if n > 2:
        x += min(x, c) * (n - 2)
print(x)
