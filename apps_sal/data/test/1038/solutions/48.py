a, b = list(map(int, input().split()))

res = 0
if a % 2 == 1:
    res ^= a
    a += 1
if b % 2 == 0:
    res ^= b
    b -= 1
print((res ^ ((b - a + 1) // 2) % 2))
