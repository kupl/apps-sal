n = int(input())
sol = n * (n - 1) * (n - 2) * (n - 3) * (n - 4)
sol = sol * sol
sol = sol // 120
print(sol)
