n = int(input())
x = 1
mn = n - 1
while x ** 2 <= n:
    if n % x == 0:
        y = n // x
        mn = min(mn, x + y - 2)
    x += 1
print(mn)
