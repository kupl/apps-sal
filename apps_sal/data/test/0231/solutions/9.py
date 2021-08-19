(n, a) = [int(x) for x in input().split()]
if a % 2 == 0:
    print(n // 2 - a // 2 + 1)
else:
    print((a + 1) // 2)
