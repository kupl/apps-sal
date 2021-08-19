foods = [int(input()) for _ in range(5)]
last = foods.pop(foods.index(min(foods, key=lambda x: (x - 1) % 10)))
print(sum(map(lambda x: (x + 9) // 10 * 10, foods)) + last)
