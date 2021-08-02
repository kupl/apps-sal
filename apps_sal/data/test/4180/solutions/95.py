pay = int(input())

if pay % 1000 == 0:
    print(0)
else:
    print((pay // 1000 + 1) * 1000 - pay)
