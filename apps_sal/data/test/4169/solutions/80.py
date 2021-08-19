(n, m) = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort()
payment = 0
for i in ab:
    price = i[0]
    amount = i[1]
    if amount > m:
        amount = m
    m -= amount
    payment += amount * price
    if m == 0:
        break
print(payment)
