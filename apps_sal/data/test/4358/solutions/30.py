total_item = int(input())
item_cost = []
for i in range(total_item):
    item_cost.append(int(input()))
print(sum(item_cost) - max(item_cost) // 2)
