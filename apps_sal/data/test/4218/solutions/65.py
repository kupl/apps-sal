n = int(input())
if n % 2 == 0:
    print(1 / 2)
elif n == 1:
    print(1)
else:
    print((n + 1) / 2 / n)
