t = int(input())

for T in range(t):
    n = int(input())
    if n % 2 == 0:
        result = n // 2
    else:
        result = (n - 1) // 2
    print(result)
