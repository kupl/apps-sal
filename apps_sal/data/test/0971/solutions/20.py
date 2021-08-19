(n, b, d) = [int(i) for i in input().split()]
oranges = [int(i) for i in input().split()]
total = 0
dispose = 0
for orange in oranges:
    if orange <= b:
        total += orange
    if total > d:
        dispose += 1
        total = 0
print(dispose)
