
ABC = list(map(int, input().split()))

total = 1
for i in ABC:
    total *= i * (i + 1) // 2

print((total % 998244353))
