N, M, X = map(int, input().split())
cost_masses = map(int, input().split())

cost_ToZero = cost_ToEnd = 0

for cost_mass in cost_masses:
    if X < cost_mass:
        cost_ToEnd = cost_ToEnd + 1
    elif X > cost_mass:
        cost_ToZero = cost_ToZero + 1
else:
  print(min([cost_ToZero, cost_ToEnd]))
