a, b, c, x, y = map(int, input().split())

piza_min = min(x, y)

plan1 = c * piza_min * 2 + a * (x - piza_min) + b * (y - piza_min)
plan2 = a * x + b * y
plan3 = c * max(x, y) * 2

print(min(plan1, plan2, plan3))
