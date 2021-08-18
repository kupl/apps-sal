n = int(input())
v = min(n, 5)
if v < 5:
    print(n * (n - 1) // 2)
    return
while v * 10 <= n:
    v *= 10
print(sum(min(n - i * v + 1, v * i - 1) for i in range(1, n // v + 1)))
