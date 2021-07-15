n, m = [int(v) for v in input().split()]

a = []
for _ in range(n):
    a.append([int(v) for v in input()])

colsums = [sum(a[i][j] for i in range(n)) for j in range(m)]

for row in a:
    if all(rv < sv for (rv, sv) in zip(row, colsums)):
        print("YES")
        return

print("NO")

