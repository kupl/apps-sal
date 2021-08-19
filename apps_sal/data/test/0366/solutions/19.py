(n, s) = list(map(int, input().split(' ')))
if s <= n:
    sol = 1
else:
    sol = s // n
    if s % n:
        sol += 1
print(sol)
