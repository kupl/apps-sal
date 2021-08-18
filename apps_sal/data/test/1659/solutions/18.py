n, x = list(map(int, input().split()))

sad = 0
for _ in range(n):
    sign, number = input().split()
    number = int(number)
    if sign == '+':
        x += number
    else:
        if number <= x:
            x -= number
        else:
            sad += 1

print(x, sad)
