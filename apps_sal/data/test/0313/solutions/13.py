n = int(input())
lst = [int(x) for x in input().split()]


atuniversity = False
break_length = 0
time = 0

for lesson in lst:
	if lesson == 1:
		atuniversity = True
		break_length = 0
	elif lesson == 0:
		break_length += 1
		if break_length >= 2:
			if atuniversity:
				time -= 1
			atuniversity = False

	if atuniversity:
		time += 1

try:
	if lst[-1] == 0 and lst[-2] == 1:
		time -= 1
except IndexError:
	pass

print(time)
