p = int(input())
count = 0
for i in range(1, p):
    (z, x) = (1, 1)
    for j in range(1, p - 1):
        x *= i
        x %= p
        if x == 1:
            z = 0
            break
    if z == 1:
        x *= i
        x %= p
        if x == 1:
            count += 1
print(count)
