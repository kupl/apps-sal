N = int(input())

power = 1

for n in range(1, N + 1):
    power = power * n % 1000000007

print(power)
