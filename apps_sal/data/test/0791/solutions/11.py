n, cell, i = int(input()), list(map(int, input().strip())), 0
while i < n - 1 and cell[i]:
    i += 1
print(i + 1)
