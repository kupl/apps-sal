N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))

square = list(range(0, N + 1))

a = square[:X + 1]
b = square[X:]

a_costs = []
b_costs = []

for i in a:
    if i in A:
        a_costs.append(i)
for i in b:
    if i in A:
        b_costs.append(i)

a_cost = len(a_costs)
b_cost = len(b_costs)

if a_cost > b_cost:
    print(b_cost)
else:
    print(a_cost)
