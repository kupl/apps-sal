a, b, c = [int(i) for i in input().split()]

sol = []

for i in range(81):
    d = b * (i**a) + c
    if d <= 0 or d >= 1000000000:
        continue
    if sum([int(j) for j in str(d)]) == i:
        sol.append(d)
print(len(sol))
sol.sort()
for i in sol:
    print(i, end=' ')
