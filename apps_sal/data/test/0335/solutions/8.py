n = int(input())
a = 1
if (n - 2) % 3 != 0:
    print(1, 1, n - 2)
elif (n - 3) % 3 != 0:
    print(1, 2, n - 3)
else:
    print(1, 3, n - 4)
