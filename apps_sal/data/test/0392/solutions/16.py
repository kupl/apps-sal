
n = int(input())

for i in range(2, min(1000001, n)):
    while n % (i * i) == 0:
        n //= i

print(n)
