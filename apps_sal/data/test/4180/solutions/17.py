n = int(input())
if n < 1000:
    print(1000 - n)
elif n % 1000 == 0:
    print(0)
else:
    x = n // 1000
    print(1000 * (x + 1) - n)
