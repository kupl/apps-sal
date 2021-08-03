n = int(input())

sol = (n // 3) * 2

if n % 3:
    sol += 1

print(sol)
