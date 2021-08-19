n = int(input())
x = int(n ** (1 / 2)) + 1
for i in range(1, x + 1):
    if n % i == 0:
        p = i
        q = n // i
print(p + q - 2)
