a = int(input())
if a % 2 != 0:
    print(0)
elif a <= 4:
    print(0)
else:
    print(a // 4 - (a % 4 == 0))
