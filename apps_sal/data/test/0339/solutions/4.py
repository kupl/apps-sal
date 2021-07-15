number = int(input())
divisor = int(input())
decrement_cost = int(input())
division_cost = int(input())

final_cost = 0
while number != 1:
	remainder = number % divisor
	if remainder != 0:
		final_cost += decrement_cost * remainder
		number -= remainder

	jump = number - number // divisor

	if division_cost < jump * decrement_cost:
		final_cost += division_cost
		number //= divisor
	else:
		final_cost += decrement_cost * (number - 1)
		number = 1

print(final_cost)
