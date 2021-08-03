n = int(input())
a = n // 1000
if n % 1000 == 0:
    print((0))
else:
    print((1000 * (a + 1) - n))
