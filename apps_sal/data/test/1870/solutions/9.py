(amount, c) = [int(i) for i in input().split()]
row = [int(i) for i in input().split()]
last = 0
counter = 0
for i in range(amount):
    if row[i] - last > c:
        counter = 1
        last = row[i]
    else:
        counter += 1
        last = row[i]
print(counter)
