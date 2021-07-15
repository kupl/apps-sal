a, b, c = map(int, input().split())

min_n = min(a, b, c)
max_n = max(a, b, c)

cost_min = (max_n - min_n)
print(cost_min)
