n, x = list(map(int, input().split()))
sad = 0
for i in range(n):
    do, amount = input().split()
    if do == '+':
        x += int(amount)
    else:
        if x >= int(amount):
            x -= int(amount)
        else:
            sad += 1
print(x, sad)

