n, m, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

mn = 0
l_cost = 0
r_cost = 0

for i in range(x):
    if i in arr:
        l_cost += 1

for i in range(x, n + 1):
    if i in arr:
        r_cost += 1

print((min(l_cost, r_cost)))
