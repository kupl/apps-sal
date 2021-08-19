A = int(input())
B = int(input())
C = int(input())
sol = 0
for a in range(1, A + 1):
    if B >= a * 2 and C >= a * 4:
        sol = max(sol, 7 * a)
print(sol)
