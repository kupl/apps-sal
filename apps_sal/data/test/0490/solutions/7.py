
n = int(input().strip())

if n == 0:
    print(0)
elif n % 2 == 1:
    print(n // 2 + 1)
else:
    print(n + 1)
