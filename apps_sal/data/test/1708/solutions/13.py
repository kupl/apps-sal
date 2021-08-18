
num_dishes, num_customers = [int(x) for x in input().split()]

dish_amounts = [int(x) for x in input().split()]
dish_costs = [int(x) for x in input().split()]

dishes_by_price = sorted(list(range(num_dishes)), key=lambda i: dish_costs[i])
dbp_i = 0

for j in range(num_customers):
    dish, amount = [int(x) for x in input().split()]
    dish -= 1
    served = min(dish_amounts[dish], amount)
    dish_amounts[dish] -= served

    cost = served * dish_costs[dish]
    not_served = amount - served

    while not_served > 0 and dbp_i != num_dishes:
        i = dishes_by_price[dbp_i]
        served = min(dish_amounts[i], not_served)
        cost += served * dish_costs[i]
        dish_amounts[i] -= served
        not_served -= served

        if dish_amounts[i] == 0:
            dbp_i += 1

    if not_served > 0:
        cost = 0

    print(cost)
