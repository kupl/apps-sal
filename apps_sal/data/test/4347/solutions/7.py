n = int(input())

res = 1
for i in range(n - 1):
    res *= (i + 1)

res //= (n // 2)
print(res)
