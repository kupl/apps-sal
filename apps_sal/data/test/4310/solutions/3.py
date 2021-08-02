a = list(map(int, input().split()))
list_int = list(a)

min_num = min(list_int)
max_num = max(list_int)
mid_num = list_int.pop(1)

minimum_cost = abs(mid_num - min_num) + abs(max_num - mid_num)
print(minimum_cost)
