a, b, c = map(int, input().split())

total = 1
for i in [a, b, c]:
    total *= i * (i + 1) // 2

print(total % 998244353)
