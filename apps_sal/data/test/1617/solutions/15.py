n = int(input())
b = set()
for i in range(1, int(n ** 0.5) + 3):
    if n % i == 0:
        v = n // i
        b.add(i * (v * (v - 1) // 2) + v)
        b.add(v * (i * (i - 1) // 2) + i)
print(*sorted(b))
