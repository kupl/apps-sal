(n, a, b) = map(int, input().split())
plan_1 = n * a
plan_2 = b
if plan_1 < plan_2:
    print(plan_1)
else:
    print(plan_2)
