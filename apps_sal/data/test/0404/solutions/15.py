b = int(input())
result = 1
count = 1
while b % 2 == 0:
    count += 1
    b >>= 1
result *= count
count = 0
i = 3
while i * i <= b:
    if b % i == 0:
        count = 1
        while b % i == 0:
            count += 1
            b //= i
        result *= count
    i += 2
if b > 1:
    result *= 2
print(result)

