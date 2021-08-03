num = int(input())
n = num
num -= 1
result = 1
for i in range(2, int(pow(num, 0.5)) + 1):
    c = 0
    while num % i == 0:
        num //= i
        c += 1
    if c > 0:
        result *= c + 1

if num > 1:
    result *= 2
result -= 1

r = set()
for i in range(2, int(pow(n, 0.5)) + 1):
    num = n
    if num % i == 0:
        r.add(i)
        r.add(n // i)
r.add(n)
for i in r:
    num = n
    while num % i == 0:
        num //= i
    if num % i == 1:
        result += 1

print(result)
