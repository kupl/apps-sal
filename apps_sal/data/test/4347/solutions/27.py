n = int(input())

f = 1
for i in range(1, n):
    f *= i

print(f // (n // 2))
