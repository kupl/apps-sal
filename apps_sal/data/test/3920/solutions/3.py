a = [int(c) for c in input().split()]
inc = a[0]
total = 0
while a[1] != 0 and a[5] != 0:
    total += 2 * inc + 1
    a[1] -= 1
    a[5] -= 1
    inc += 1
if a[1] == 0 and a[5] == 0:
    inc -= 1
    for i in range(a[2]):
        total += 2 * inc + 1
        inc -= 1
else:
    b = max(a[1], a[5])
    for i in range(b):
        total += 2 * inc
    inc -= 1
    for i in range(min(a[2], a[4])):
        total += 2 * inc + 1
        inc -= 1
print(total)
