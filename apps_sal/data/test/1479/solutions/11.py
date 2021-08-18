n, m, k = list(map(int, input().split()))
field = []
counts = []
for j in range(m):
    counts.append(0)
for i in range(n):
    row = list(input())
    field.append(row)

for i in range(n):
    for j in range(m):
        if field[i][j] == "L":
            jth = j - i
            if jth >= 0:
                counts[jth] += 1
        elif field[i][j] == "R":
            jth = i + j
            if jth < m:
                counts[jth] += 1
        elif field[i][j] == "U":
            if i % 2 == 0:
                counts[j] += 1


print(" ".join(list(map(str, counts))))
