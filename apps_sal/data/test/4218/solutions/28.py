n = int(input())
if n == 1:
    print(1)
    return
if n % 2 == 0: print(0.5)
else: print((n // 2 + 1) / n)
