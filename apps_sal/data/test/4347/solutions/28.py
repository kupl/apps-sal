n = int(input())
t = 1
for i in range(n):
    t *= i + 1
print(t // (n * n // 2))
