n = int(input())
x = 2
while n % x > 0:
    x += 1
print("{}{}".format(x, n // x))
