n = int(input())
if n % 1000 == 0:
    print(0)
else:
    print((n // 1000 + 1) * 1000 - n)
