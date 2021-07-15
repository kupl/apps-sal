n = int(input())

if n < 2:
    print(1)
elif n < 4:
    print(2)
elif n < 8:
    print(4)
elif n < 16:
    print(8)
elif n < 32:
    print(16)
elif n < 64:
    print(32)
else:
    print(64)
