n = int(input())
n += 3600000000000000000
n %= 360
if n <= 45:
    print(0)
elif n <= 135:
    print(1)
elif n <= 225:
    print(2)
elif n < 315:
    print(3)
else:
    print(0)
