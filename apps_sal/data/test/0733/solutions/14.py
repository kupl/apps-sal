(x, y, a, b) = (int(i) for i in input().split())
p = 1
for i in range(2, 1001):
    if x % i == 0 and y % i == 0:
        x = x // i
        y = y // i
        p *= i
print(b // (x * y * p) - (a - 1) // (x * y * p))
