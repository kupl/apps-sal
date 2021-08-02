n = int(input())
if n == 0:
    print(0)
if n % 2 == 0 and n > 0:
    print(n + 1)
if n % 2 == 1:
    print((n + 1) // 2)
