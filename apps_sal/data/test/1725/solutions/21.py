n, m, d = [int(x) for x in input().split(' ')]

total = n * m
total_matrix = []

for i in range(n):
    total_matrix += [int(x) for x in input().split(' ')]

total_matrix = sorted(total_matrix)

middle = total // 2
not_possible = False
count = 0

for el in total_matrix:
    if abs(total_matrix[middle] - el) % d != 0:
        not_possible = True
        break
    else:
        count += abs(total_matrix[middle] - el) // d

if not_possible:
    print(-1)
else:
    print(count)
