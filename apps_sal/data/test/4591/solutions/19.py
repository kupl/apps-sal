a_price,b_price,ab_price,num_a,num_b = list(map(int, input().split()))
total = 0

if a_price + b_price < 2 * ab_price:
	total = a_price * num_a + b_price * num_b

elif a_price + b_price >= 2 * ab_price:
	if num_a >= num_b:
		if a_price > ab_price * 2:
			total = ab_price * 2 * num_a
		else:
			total = ab_price * 2 * num_b + a_price * (num_a - num_b)
	else:
		if b_price > ab_price * 2:
			total = ab_price * 2 * num_b
		else:
			total = ab_price * 2 * num_a + b_price * (num_b - num_a)

print(total)


