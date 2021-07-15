n = int(input())
file_name = input()

to_remove = 0
current_streak = 0

for i in range(n):
	if file_name[i] != 'x':
		current_streak = 0
		continue
	else:
		current_streak += 1
		if current_streak > 2:
			to_remove += 1


print(to_remove)
