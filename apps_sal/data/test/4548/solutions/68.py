n, m, x = map(int, input().split())
lst = list(map(int, input().split()))

a_cost = 0
b_cost = 0
for i in lst:
    if i > x:
        a_cost += 1
    else:
        b_cost += 1
print(min(a_cost, b_cost))
