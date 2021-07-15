n = int(input())
if n % 2:
    print(0)
else:
    n //= 2
    print((n - 1) // 2)
