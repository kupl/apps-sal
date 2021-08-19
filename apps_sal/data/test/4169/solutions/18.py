(n, m) = map(int, input().split())
shop = [[int(i) for i in input().split()] for _ in range(n)]
shop = list(sorted(shop, key=lambda x: x[0]))
count = 0
money = 0
for x in shop:
    count += x[1]
    money += x[0] * x[1]
    if count >= m:
        excess = count - m
        money -= x[0] * excess
        break
print(money)
