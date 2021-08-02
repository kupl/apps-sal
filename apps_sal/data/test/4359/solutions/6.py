foods = [int(input()) for _ in range(5)]
order_times = [food - food % 10 + 10 if food % 10 != 0 else food for food in foods]
diff = [(order_time - food) for order_time, food in zip(order_times, foods)]

print((sum(order_times) - max(diff)))
