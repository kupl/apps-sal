n = int(input())
x = 0
x += (n // 2520) * 576
for i in range(1, n % 2520 + 1):
    d = True
    for j in range(2, 11):
        if i % j == 0:
            d = False
            break
    if d:
        x += 1
print(x)
