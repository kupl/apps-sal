n, r = map(int, input().split())
heaters = list(map(int, input().split()))

count = 0
position = 0
last_seen_heater = -1

while position < n:
	index = last_seen_heater + 1
	while index < position + r and index < n:
		if heaters[index] == 1:
			last_seen_heater = index
		index += 1
	# print(position, last_seen_heater)
	new_pos = position
	if last_seen_heater >= 0:
		new_pos = last_seen_heater + r
	if new_pos != position:
		position = new_pos
		count += 1
	else:
		count = -1
		break

print(count)
