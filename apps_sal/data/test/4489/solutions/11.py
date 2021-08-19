n = int(input())
blues = [input() for _ in range(n)]
m = int(input())
reds = [input() for _ in range(m)]
max_price = 0
for blue in blues:
    plus = len(list([x for x in blues if x == blue]))
    minus = len(list([x for x in reds if x == blue]))
    price = plus - minus
    if price > max_price:
        max_price = price
print(max_price)
