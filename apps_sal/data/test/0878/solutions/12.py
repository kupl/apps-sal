input()

points = 0

line = input()

shapes = list(map(int, line.split()))

# circle = 1
# triangle = 2
# square = 3

for a, b in zip(shapes, shapes[1:]):
	if a == 1 or b == 1:
		points += a + b
	else:
		points = -1
		break

if points == -1:
	print("Infinite")
else:
	print("Finite")
	print(points - line.count("3 1 2"))
