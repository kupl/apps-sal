n = int(input())
v = list(map(int, input().split()))
sol = 'YES'

for x in v:
    if v.count(x) * 2 > n + 1:
        sol = 'NO'

print(sol)
