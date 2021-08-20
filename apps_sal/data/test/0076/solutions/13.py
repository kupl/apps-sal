(n, m, a, b) = [int(v) for v in input().split()]
down = n // m * m
up = (n + m - 1) // m * m
cost_down = (n - down) * b
cost_up = (up - n) * a
print(min(cost_down, cost_up))
