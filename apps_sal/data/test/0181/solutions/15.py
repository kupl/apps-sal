n = int(input())
n += 3600000000000000000000
x = n % 360
if x <= 45:
    print(0)
elif x <= 135:
    print(1)
elif x <= 225:
    print(2)
elif x < 315:
    print(3)
elif x >= 315:
    print(0)
