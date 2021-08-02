n, m, x = list(map(int, input().split()))
a_lst = list(map(int, input().split()))

cost1 = 0
cost2 = 0
for i in range(x, n + 1):
    if i in a_lst:
        cost1 += 1
for i in range(x, -1, -1):
    if i in a_lst:
        cost2 += 1
print((min(cost1, cost2)))
