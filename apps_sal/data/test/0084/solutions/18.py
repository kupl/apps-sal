n = int(input())
a = 5
while a * 10 <= n:
    a *= 10
print(sum(min(n - i * a + 1, a * i - 1) for i in range(1, n // a + 1)) if n >= 5 else n * (n - 1) // 2)
