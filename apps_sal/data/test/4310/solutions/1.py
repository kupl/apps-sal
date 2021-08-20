lst = input().split()
costs = []
for a in [[0, 1], [0, 2], [1, 2]]:
    costs.append(abs(int(lst[a[0]]) - int(lst[a[1]])))
print(sum(costs) - max(costs))
