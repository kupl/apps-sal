N = int(input())
num_list = list(map(int, input().split()))
cost_list = []
max_num = max(num_list)
min_num = min(num_list)

for i in range(min_num, max_num):
    cost = 0
    for j in num_list:
        cost += (i - j)**2
    cost_list.append(cost)

if len(cost_list) == 0:
    cost_list.append(0)

print(min(cost_list))
