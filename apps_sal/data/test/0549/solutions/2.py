n = int(input())
rowres = 1
for row in range(1, n + 1):
    if n % row == 0:
        col = n // row
        if row <= col:
            rowres = row
print(rowres, n // rowres)
