n = (int(input()) + 45) % 360
if n % 90 == 0 and n != 0:
    print(n // 90 - 1)
else:
    print(n // 90)
