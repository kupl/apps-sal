n = int(input())
power = 1
for i in range(1, n + 1):
    power *= i
    power = power % (10**9 + 7)
print(power)
