a = int(input())
if (a // 100) % 9 == 0:
    b = 100
else:
    b = 900
if ((a - (a // 100) * 100) // 10) % 9 == 0:
    c = 10
else:
    c = 90
if (a - (a // 10) * 10) % 9 == 0:
    d = 1
else:
    d = 9
print(b + c + d)
