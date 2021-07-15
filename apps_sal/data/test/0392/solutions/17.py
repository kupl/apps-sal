n = int(input())

sol = 1
i = 2

while i*i <= n:
    if n % i == 0:
        sol *= i
    while n % i == 0:
        n //= i
    i += 1

if n != 1 and sol % n != 0:
    sol *= n

print(sol)

