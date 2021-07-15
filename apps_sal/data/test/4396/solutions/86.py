N = int(input())
moneys = [tuple(map(str, input().split())) for _ in range(N)]
rate = 380000

total = 0
for money in moneys:
    x, u = money
    x = float(x)
    if u == 'JPY':
        total += x
    else:
        total += x * rate

print(total)


