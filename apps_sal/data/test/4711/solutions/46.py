(a, b, c) = map(int, input().split())
plan1 = a + b
plan2 = b + c
plan3 = c + a
print(min(plan1, plan2, plan3))
