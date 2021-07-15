n = int(input())

for i in range(2, n + 1):
    if n % i == 0:
        if i == 2:
            print(n // i)
            return
        else:
            print(1 + (n - i) // 2)
            return
    if i * i > n * 2:
        break

print(1 if n > 0 else 0)

