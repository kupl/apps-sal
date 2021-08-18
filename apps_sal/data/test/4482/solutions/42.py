N = int(input())
int_list = [int(x) for x in input().split()]


def calc_cost(int_list, y):
    cost = 0
    for x in int_list:
        cost += (x - y)**2
    return cost


cost_list = [calc_cost(int_list, y) for y in range(min(int_list), max(int_list) + 1)]
print(min(cost_list))
