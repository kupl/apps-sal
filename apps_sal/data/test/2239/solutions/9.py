n = int(input())
for i in range(n):
    x = int(input())
    sol = 0
    if x % 2 == 1:
        sol += 1
        x -= 3
    sol += x // 2
    print(sol)
