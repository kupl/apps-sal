x = int(input())
a = x // 11
b = x % 11
if b == 0:
    print(a * 2)
elif b <= 6:
    print(a * 2 + 1)
else:
    print(a * 2 + 2)
