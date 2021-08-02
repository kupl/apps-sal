n, x = list(map(int, input().split()))
distress = 0
for _ in range(n):
    c, amount = input().split()
    amount = int(amount)
    if c == '-':
        if amount <= x:
            x -= amount
        else:
            distress += 1
    else:
        x += amount
print(str(x) + " " + str(distress))
