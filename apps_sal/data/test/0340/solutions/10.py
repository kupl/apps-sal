n = int(input())
num = 1
maxPow = 1
minPow = 9999
for i in range(2, n + 1):
    if n % i == 0:
        power = 0
        while n % i == 0:
            power += 1
            n = n // i
        num *= i
        maxPow = max(maxPow, power)
        minPow = min(minPow, power)
i = 1
power = 0
while i < maxPow:
    i *= 2
    power += 1
if i != maxPow:
    power += 1
elif minPow < maxPow:
    power += 1
print(num, power)
